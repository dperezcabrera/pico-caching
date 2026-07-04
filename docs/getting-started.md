# Getting Started

## Install

```bash
pip install pico-caching
```

## Basic usage

```python
@cacheable                       # default TTL (cache.default_ttl_seconds)
def find(self, user_id): ...

@cacheable(ttl_seconds=5)        # per-method TTL
def hot(self): ...

@cacheable(key=lambda q: f"s:{q}")   # custom key from the call args
def search(self, q): ...
```

Sync and async both work; for async methods the **awaited result** is cached,
never the coroutine. The default key includes class, method and the repr of
every argument — same args, same entry.

## Settings

```yaml
cache:
  enabled: true
  default_ttl_seconds: 300
  max_entries: 1024      # built-in LRU eviction bound
```

## Custom backend

Implement the protocol as a `@component` — it replaces the built-in
automatically:

```python
from pico_ioc import component

@component
class RedisBackend:  # satisfies CacheBackend
    def get(self, key): ...      # -> (hit: bool, value)
    def set(self, key, value, ttl_seconds): ...
    def delete(self, key): ...
    def clear(self): ...
```
