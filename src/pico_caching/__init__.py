"""pico-caching: declarative caching for the Pico ecosystem.

``@cacheable`` over pico-ioc method interception, with a pluggable
``CacheBackend`` protocol and a built-in thread-safe in-memory LRU with TTL.
Auto-discovered by pico-boot; zero-config (no ``cache:`` block required).

Public API:
    Decorator: cacheable
    Protocol: CacheBackend
    Backend: InMemoryCacheBackend
    Settings: CacheSettings
"""

from .backend import CacheBackend, InMemoryCacheBackend
from .config import CacheSettings
from .decorators import cacheable
from .interceptor import CacheInterceptor

__all__ = ["cacheable", "CacheBackend", "InMemoryCacheBackend", "CacheSettings", "CacheInterceptor"]
