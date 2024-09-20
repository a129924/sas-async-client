from pytest import mark


@mark.asyncio
async def test_get_sas_access_token():
    from src.sas_async_client._utils.connection_utils import get_sas_api_connect_config
    from src.sas_async_client.core._httpx import create_async_web_session
    from src.sas_async_client.core.sas.auth import get_sas_access_token
    from src.sas_async_client.types.oauth import OAuthToken

    config = get_sas_api_connect_config()

    async with create_async_web_session() as client:
        token = await get_sas_access_token(
            client,
            config.sas_api_connect_url,
            config.sas_api_connect_username,
            config.sas_api_connect_password,
        )

        assert isinstance(token, OAuthToken)
        assert token.access_token
        assert token.token_type == "bearer"
        assert token.id_token
        assert token.refresh_token
        assert token.expires_in
        assert token.scope
        assert token.jti
