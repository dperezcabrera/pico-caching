"""``@cacheable`` marker: stores the policy and attaches the interceptor."""

from typing import Any, Callable

CACHE_META = "_pico_caching_meta"


def cacheable(
    _func: Callable | None = None,
    *,
    ttl_seconds: float | None = None,
    key: Callable[..., str] | None = None,
):
    """Cache the method's return value. Sync or async; async methods cache
    the awaited result, never the coroutine. ``key(*args, **kwargs)``
    overrides the default repr-based key; ``ttl_seconds`` overrides
    ``cache.default_ttl_seconds``."""

    def dec(fn):
        setattr(fn, CACHE_META, {"ttl_seconds": ttl_seconds, "key": key})
        from pico_ioc import intercepted_by

        from .interceptor import CacheInterceptor

        return intercepted_by(CacheInterceptor)(fn)

    return dec(_func) if callable(_func) else dec


def _meta(ctx: Any) -> dict:
    fn = getattr(ctx.cls, ctx.name, None)
    return getattr(fn, CACHE_META, {})
