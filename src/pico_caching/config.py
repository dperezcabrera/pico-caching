"""Settings for pico-caching (prefix ``caching``, zero-config)."""

from dataclasses import dataclass

from pico_ioc import configured


@configured(target="self", prefix="caching", mapping="tree")
@dataclass
class CacheSettings:
    """``enabled: false`` makes ``@cacheable`` a pass-through."""

    enabled: bool = True
    default_ttl_seconds: float = 300.0
    max_entries: int = 1024
