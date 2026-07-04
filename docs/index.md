# pico-caching

Part of an ecosystem [built for the AI era](https://dperezcabrera.github.io/pico-ioc/ai-ready/):
machine-readable conventions in every repo, installable
[AI coding skills](https://github.com/dperezcabrera/pico-skills), and
[scaffolds](https://dperezcabrera.github.io/pico-initializer/) that generate
AI-maintainable projects.

Declarative method caching over [pico-ioc](https://github.com/dperezcabrera/pico-ioc)
interception: `@cacheable`, pluggable backends, built-in thread-safe LRU with
TTL. Auto-discovered by pico-boot; zero-config.

## 30-second example

```python
from pico_ioc import component
from pico_caching import cacheable

@component
class UserRepo:
    @cacheable(ttl_seconds=60)
    async def find(self, user_id: int): ...
```

Continue with [Getting Started](getting-started.md).
