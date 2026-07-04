Read and follow ./AGENTS.md for project conventions.

## Pico Ecosystem Context

pico-caching provides `@cacheable` via pico-ioc `MethodInterceptor` with a pluggable `CacheBackend` protocol (built-in thread-safe in-memory LRU + TTL). Same decorator idiom as pico-pydantic. Auto-discovered via `pico_boot.modules` entry point. Config prefix `cache` (zero-config).

## Key Reminders

- pico-ioc dependency: `>= 2.2.0`
- **NEVER change `version_scheme`** in pyproject.toml. It MUST remain `"post-release"`.
- requires-python >= 3.11
- Commit messages: one line only
- Async methods cache the awaited result, never the coroutine
- A user `CacheBackend` @component replaces the built-in (selection in `CacheInterceptor.__init__`)
