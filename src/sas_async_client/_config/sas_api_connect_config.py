from pydantic_settings import BaseSettings, SettingsConfigDict


class SasApiConnectConfig(BaseSettings):
    """
    Configuration for SAS API Connect.

    Args:
        sas_api_connect_url (str): URL for SAS API Connect.
        sas_api_connect_username (str): Username for SAS API Connect.
        sas_api_connect_password (str): Password for SAS API Connect.
    """

    sas_api_connect_url: str
    sas_api_connect_username: str
    sas_api_connect_password: str

    model_config = SettingsConfigDict(
        env_prefix="SAS_API_CONNECT_", env_file="sas_api_connect.env"
    )
