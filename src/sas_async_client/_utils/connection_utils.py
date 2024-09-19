from functools import lru_cache

from .._config import SasApiConnectConfig


@lru_cache(maxsize=1)
def get_sas_api_connect_config() -> SasApiConnectConfig:
    return SasApiConnectConfig()  # type: ignore
