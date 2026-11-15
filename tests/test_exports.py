"""The public API is exactly what ``__all__`` declares (stability contract)."""

import pico_caching


def test_public_api_is_declared_and_importable():
    assert set(pico_caching.__all__) == {
        "CacheBackend",
        "CacheInterceptor",
        "CacheSettings",
        "InMemoryCacheBackend",
        "cacheable",
    }
    for name in pico_caching.__all__:
        assert getattr(pico_caching, name) is not None
