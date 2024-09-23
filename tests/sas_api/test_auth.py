from pytest import fixture as sync_fixture
from pytest import mark
from pytest_asyncio import fixture as async_fixture


@async_fixture(scope="module")
async def client():
    from src.sas_async_client.core._httpx import create_async_web_session

    async with create_async_web_session() as client:
        yield client  # 返回 client 供測試使用


@sync_fixture(scope="module")
def config():
    from src.sas_async_client._utils.connection_utils import get_sas_api_connect_config

    return get_sas_api_connect_config()  # 返回配置供測試使用


@async_fixture(scope="module")
async def token(client, config):
    from src.sas_async_client.core.sas.auth import get_sas_access_token
    from src.sas_async_client.types.oauth import OAuthToken

    token = await get_sas_access_token(
        async_web_session=client,
        base_url=config.sas_api_connect_url,
        user_id=config.sas_api_connect_username,
        user_password=config.sas_api_connect_password,
    )

    assert isinstance(token, OAuthToken)
    assert token.access_token
    assert token.token_type == "bearer"
    assert token.id_token
    assert token.refresh_token
    assert token.expires_in
    assert token.scope
    assert token.jti

    return token


@async_fixture(scope="module")
async def cas_session_id(token, client, config):
    from src.sas_async_client.core.sas.cas import get_cas_session_id

    cas_session = await get_cas_session_id(
        async_web_session=client,
        sas_oauth_token=token.access_token,
        base_url=config.sas_api_connect_url,
    )
    return cas_session  # 返回 CAS session ID


@mark.asyncio
async def test_get_sas_access_token(token):
    assert token


@mark.asyncio
async def test_create_cas_session(cas_session_id):
    assert cas_session_id


@mark.asyncio
async def test_get_cas_session_info(cas_session_id, token, config):
    from src.sas_async_client.core._httpx import create_async_web_session
    from src.sas_async_client.core.sas.cas import get_cas_session_info

    async with create_async_web_session(verify=False) as client:
        session_info = await get_cas_session_info(
            async_web_session=client,
            sas_oauth_token=token.access_token,
            base_url=config.sas_api_connect_url,
            cas_session_id=cas_session_id,
        )
        assert session_info
        assert session_info.id_
        assert session_info.uuid
        assert session_info.name
        assert session_info.state
        assert session_info.httpPort == 0
        assert session_info.httpProtocol
        assert session_info.user
        assert session_info.owner
        assert session_info.provider


@mark.asyncio
async def test_delete_cas_session(cas_session_id, token, config):
    from src.sas_async_client.core._httpx import create_async_web_session
    from src.sas_async_client.core.sas.cas import delete_cas_session

    async with create_async_web_session(verify=False) as client:
        result = await delete_cas_session(
            async_web_session=client,
            sas_oauth_token=token.access_token,
            base_url=config.sas_api_connect_url,
            cas_session_id=cas_session_id,
        )

        assert result is None
