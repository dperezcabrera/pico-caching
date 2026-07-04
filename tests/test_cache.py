import asyncio
import sys
import time

from pico_ioc import component

from pico_caching import CacheSettings, InMemoryCacheBackend, cacheable


@component
class Repo:
    def __init__(self):
        self.calls = 0

    @cacheable
    def find(self, user_id: int):
        self.calls += 1
        return {"id": user_id}

    @cacheable(ttl_seconds=0.05)
    def short_lived(self):
        self.calls += 1
        return self.calls

    @cacheable(key=lambda user_id: f"user:{user_id}")
    async def afind(self, user_id: int):
        self.calls += 1
        return {"id": user_id, "async": True}


def test_sync_hit_and_per_args_keys(make_container):
    repo = make_container(sys.modules[__name__]).get(Repo)
    assert repo.find(1) == {"id": 1}
    assert repo.find(1) == {"id": 1}
    assert repo.calls == 1
    repo.find(2)
    assert repo.calls == 2


def test_ttl_expires(make_container):
    repo = make_container(sys.modules[__name__]).get(Repo)
    assert repo.short_lived() == 1
    assert repo.short_lived() == 1
    time.sleep(0.06)
    assert repo.short_lived() == 2


def test_async_caches_result_not_coroutine(make_container):
    repo = make_container(sys.modules[__name__]).get(Repo)

    async def run():
        a = await repo.afind(7)
        b = await repo.afind(7)
        return a, b

    a, b = asyncio.run(run())
    assert a == b == {"id": 7, "async": True}
    assert repo.calls == 1


def test_disabled_bypasses_cache(make_container):
    repo = make_container(sys.modules[__name__], enabled=False).get(Repo)
    repo.find(1)
    repo.find(1)
    assert repo.calls == 2


def test_lru_eviction():
    backend = InMemoryCacheBackend(CacheSettings(max_entries=2))
    backend.set("a", 1, 60)
    backend.set("b", 2, 60)
    backend.get("a")
    backend.set("c", 3, 60)
    assert backend.get("b") == (False, None)
    assert backend.get("a") == (True, 1)
    assert backend.get("c") == (True, 3)
