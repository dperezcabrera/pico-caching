import pytest
from pico_ioc import DictSource, configuration, init


@pytest.fixture
def make_container():
    created = []

    def _make(module, **cache_cfg):
        cfg = configuration(DictSource({"caching": cache_cfg}))
        c = init(modules=["pico_caching", module], config=cfg)
        created.append(c)
        return c

    yield _make
    for c in created:
        c.shutdown()
