# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-07-03

### Added

- `@cacheable` decorator (sync + async; the awaited result is cached).
- `CacheBackend` protocol; user backends replace the built-in automatically.
- `InMemoryCacheBackend`: thread-safe LRU with per-entry TTL.
- `CacheSettings` (prefix `cache`): `enabled`, `default_ttl_seconds`, `max_entries`.
- Auto-discovery through the `pico_boot.modules` entry point; zero-config.

[Unreleased]: https://github.com/dperezcabrera/pico-caching/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/dperezcabrera/pico-caching/releases/tag/v0.1.0
