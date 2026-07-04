# pico-caching

Declarative caching (@cacheable) for pico-ioc components with pluggable backends.

## Commands

```bash
pip install -e ".[dev]"
pytest tests/ -v
pytest --cov=pico_caching --cov-report=term-missing tests/
mkdocs serve -f mkdocs.yml
```

## Project Structure

```
src/pico_caching/
  __init__.py     # Public API
  decorators.py   # @cacheable (policy on fn + intercepted_by)
  interceptor.py  # CacheInterceptor (get-or-compute)
  backend.py      # CacheBackend protocol + InMemoryCacheBackend (LRU + TTL)
  config.py       # CacheSettings (prefix "cache")
```

## Key Concepts

- Default key: module.Class.method(args;kwargs) repr; override with `key=callable`.
- TTL: per-decorator `ttl_seconds` overrides `cache.default_ttl_seconds`.
- Backend selection: first non-builtin `CacheBackend` component wins, else built-in LRU.
- Async caches the awaited result; `time.monotonic` for expiry; one lock, OrderedDict LRU.
- `cache.enabled: false` -> pass-through.

## Boundaries

- Do not modify `_version.py`
- Keep `backend.py` free of asyncio (backends are sync by contract)
