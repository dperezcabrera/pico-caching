# Troubleshooting

## The cache never hits

- The method must run through the container proxy (`@component` class,
  resolved via DI) — direct instances bypass interception.
- Check the key: default is repr-based. Arguments whose `repr` changes every
  call (objects without `__repr__`) never repeat a key — pass
  `key=lambda ...`.

## Hits happen but data is stale

TTL. Lower `ttl_seconds` on the decorator or `caching.default_ttl_seconds`,
or invalidate: inject your backend and `delete(key)` / `clear()`.

## Entries disappear before their TTL

LRU eviction: `caching.max_entries` (default 1024) bounds the built-in
backend. Raise it or shard hot methods to a custom backend.

## Combining with @retryable

`@retryable` on top, `@cacheable` below — otherwise the retried success is
not stored (see pico-resilience's chain rule).
