"""Cache backend protocol and the built-in in-memory LRU backend."""

import threading
import time
from collections import OrderedDict
from typing import Any, Protocol, Tuple, runtime_checkable

from pico_ioc import component

from .config import CacheSettings

_MISS = object()


@runtime_checkable
class CacheBackend(Protocol):
    """Implement as a ``@component`` to replace the in-memory backend."""

    def get(self, key: str) -> Tuple[bool, Any]: ...
    def set(self, key: str, value: Any, ttl_seconds: float) -> None: ...
    def delete(self, key: str) -> None: ...
    def clear(self) -> None: ...


@component
class InMemoryCacheBackend:
    """Thread-safe LRU with per-entry TTL (``time.monotonic`` based)."""

    def __init__(self, settings: CacheSettings):
        self._max = settings.max_entries
        self._data: OrderedDict[str, Tuple[float, Any]] = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: str) -> Tuple[bool, Any]:
        with self._lock:
            item = self._data.get(key, _MISS)
            if item is _MISS:
                return False, None
            expires_at, value = item
            if time.monotonic() >= expires_at:
                del self._data[key]
                return False, None
            self._data.move_to_end(key)
            return True, value

    def set(self, key: str, value: Any, ttl_seconds: float) -> None:
        with self._lock:
            self._data[key] = (time.monotonic() + ttl_seconds, value)
            self._data.move_to_end(key)
            while len(self._data) > self._max:
                self._data.popitem(last=False)

    def delete(self, key: str) -> None:
        with self._lock:
            self._data.pop(key, None)

    def clear(self) -> None:
        with self._lock:
            self._data.clear()
