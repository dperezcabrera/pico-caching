# Learning Roadmap

1. **Install** — `pip install pico-caching`
   ([Getting Started](getting-started.md)).
2. **First hit** — `@cacheable` on an expensive lookup; verify with a call
   counter that the second call is free.
3. **Tune TTL** — per-method `ttl_seconds` vs `caching.default_ttl_seconds`.
4. **Custom keys** — `key=lambda user_id: f"user:{user_id}"` when reprs are
   noisy.
5. **Your backend** — implement `CacheBackend` as a `@component` (Redis,
   memcached); it replaces the built-in automatically
   ([Architecture](architecture.md)).
6. **Invalidate** — inject the backend; `delete`/`clear` until
   `@cache_evict` exists.
