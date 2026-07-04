"""Cache interceptor: get-or-compute through the selected backend."""

import inspect
from typing import Any, Callable, List

from pico_ioc import MethodCtx, component

from .backend import CacheBackend, InMemoryCacheBackend
from .config import CacheSettings
from .decorators import _meta


def _default_key(ctx: MethodCtx) -> str:
    kw = ",".join(f"{k}={v!r}" for k, v in sorted(ctx.kwargs.items()))
    return f"{ctx.cls.__module__}.{ctx.cls.__qualname__}.{ctx.name}({','.join(map(repr, ctx.args))};{kw})"


@component(scope="singleton")
class CacheInterceptor:
    """Uses the first user-provided ``CacheBackend``; falls back to the
    built-in in-memory LRU."""

    def __init__(self, settings: CacheSettings, backends: List[CacheBackend]):
        self.settings = settings
        custom = [b for b in backends if not isinstance(b, InMemoryCacheBackend)]
        fallback = [b for b in backends if isinstance(b, InMemoryCacheBackend)]
        self.backend = (custom or fallback)[0]

    def invoke(self, ctx: MethodCtx, call_next: Callable[[MethodCtx], Any]) -> Any:
        meta = _meta(ctx)
        if not self.settings.enabled or not meta:
            return call_next(ctx)
        key_fn = meta["key"]
        key = key_fn(*ctx.args, **ctx.kwargs) if key_fn else _default_key(ctx)
        ttl = meta["ttl_seconds"] if meta["ttl_seconds"] is not None else self.settings.default_ttl_seconds
        if inspect.iscoroutinefunction(ctx.method):
            return self._get_or_compute_async(ctx, call_next, key, ttl)
        hit, value = self.backend.get(key)
        if hit:
            return value
        value = call_next(ctx)
        self.backend.set(key, value, ttl)
        return value

    async def _get_or_compute_async(self, ctx, call_next, key: str, ttl: float):
        hit, value = self.backend.get(key)
        if hit:
            return value
        value = await call_next(ctx)
        self.backend.set(key, value, ttl)
        return value
