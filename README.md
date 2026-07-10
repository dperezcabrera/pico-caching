# pico-caching

[![PyPI](https://img.shields.io/pypi/v/pico-caching.svg)](https://pypi.org/project/pico-caching/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/dperezcabrera/pico-caching)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![CI (tox matrix)](https://github.com/dperezcabrera/pico-caching/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/dperezcabrera/pico-caching/branch/main/graph/badge.svg)](https://codecov.io/gh/dperezcabrera/pico-caching)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dperezcabrera_pico-caching&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=dperezcabrera_pico-caching)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=dperezcabrera_pico-caching&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=dperezcabrera_pico-caching)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=dperezcabrera_pico-caching&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=dperezcabrera_pico-caching)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pico-caching)](https://pypi.org/project/pico-caching/)
[![Docs](https://img.shields.io/badge/Docs-pico--caching-blue?style=flat&logo=readthedocs&logoColor=white)](https://dperezcabrera.github.io/pico-caching/)
[![Interactive Lab](https://img.shields.io/badge/Learn-online-green?style=flat&logo=python&logoColor=white)](https://dperezcabrera.github.io/pico-learn/)

Declarative **method caching** for the [Pico](https://github.com/dperezcabrera/pico-ioc) ecosystem: `@cacheable` over pico-ioc method interception, pluggable backends, auto-discovered by [pico-boot](https://github.com/dperezcabrera/pico-boot). Zero-config.

## Install

```bash
pip install pico-caching
```

## Use

```python
from pico_ioc import component
from pico_caching import cacheable

@component
class UserRepo:
    @cacheable(ttl_seconds=60)
    async def find(self, user_id: int): ...

    @cacheable(key=lambda q: f"search:{q}")
    def search(self, q: str): ...
```

Sync and async (the awaited **result** is cached, never the coroutine). Default backend: thread-safe in-memory LRU with per-entry TTL (`caching.max_entries`, `caching.default_ttl_seconds`). Bring your own backend by implementing the `CacheBackend` protocol as a `@component` — it replaces the built-in automatically.

```yaml
# application.yaml (optional)
caching:
  default_ttl_seconds: 300
  max_entries: 1024
```

Skipped for now: `@cache_evict` and a Redis backend — planned once real usage asks for them.

## Documentation

Full docs at **[dperezcabrera.github.io/pico-caching](https://dperezcabrera.github.io/pico-caching/)**.

## AI Coding Skills

Install [Claude Code](https://code.claude.com) or [OpenAI Codex](https://openai.com/index/introducing-codex/) skills for AI-assisted development with pico-caching:

```bash
curl -sL https://raw.githubusercontent.com/dperezcabrera/pico-skills/main/install.sh | bash
```

The `pico-conventions` skill teaches the assistant this module's API surface and invariants; `/add-component` and `/add-tests` scaffold components and tests that use it.

## License

MIT
