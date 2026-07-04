"""Settings for pico-caching (prefix ``cache``, zero-config)."""

from dataclasses import dataclass

from pico_ioc import configured


@configured(target="self", prefix="cache", mapping="tree")
@dataclass
class CacheSettings:
    """``enabled: false`` makes ``@cacheable`` a pass-through."""

    enabled: bool = True
    default_ttl_seconds: float = 300.0
    max_entries: int = 1024
