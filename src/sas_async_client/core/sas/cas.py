from httpx import AsyncClient

from ...schema.session_model import SessionModel
from ...types.oauth import OAuthToken


async def get_sas_oauth_token(
    async_web_session: AsyncClient,
    base_url: str,
    user_id: str,
    user_password: str,
) -> OAuthToken:
    """
    Get the SAS OAuth token.
    """
    from ...core.sas.auth import get_sas_access_token

    return await get_sas_access_token(
        async_web_session,
        base_url,
        user_id,
        user_password,
    )


async def get_cas_session_id(
    async_web_session: AsyncClient,
    sas_oauth_token: str,
    base_url: str,
) -> str:
    """
    Get the CAS session ID.

    Args:
        async_web_session: The async web session.
        sas_oauth_token: The SAS OAuth token.
        base_url: The base URL.

    Returns:
        The CAS session ID.

    Raises:
        ValueError: If the CAS session ID is not found.

    Example:
        >>> async_web_session = create_async_web_session()
        >>> sas_oauth_token = await get_sas_oauth_token(
            async_web_session,
            base_url,
            user_id,
            user_password,
        )
        >>> cas_session_id = await get_cas_session_id(
            async_web_session,
            sas_oauth_token,
            base_url,
        )
    """
    from ...core.sas.headers import sas_cas_get_session_id_post_headers
    from ...core.sas.url_generators import generate_cas_session_url

    url = generate_cas_session_url(base_url=base_url)
    response = await async_web_session.post(
        url,
        headers=sas_cas_get_session_id_post_headers(access_token=sas_oauth_token),
    )

    if response.status_code != 200:
        raise ValueError(
            f"Failed to get CAS session ID: {response.text}, error url: {url}"
        )

    return response.json()["session"]


async def delete_cas_session(
    async_web_session: AsyncClient,
    sas_oauth_token: str,
    base_url: str,
    cas_session_id: str,
) -> None:
    """
    Delete the CAS session.

    Args:
        async_web_session: The async web session.
        sas_oauth_token: The SAS OAuth token.
        base_url: The base URL.
        cas_session_id: The CAS session ID.

    Returns:
        None
    """
    from ...core.sas.headers import sas_cas_shutdown_delete_headers
    from ...core.sas.url_generators import generate_cas_session_id_url

    response = await async_web_session.delete(
        generate_cas_session_id_url(base_url=base_url, cas_session_id=cas_session_id),
        headers=sas_cas_shutdown_delete_headers(access_token=sas_oauth_token),
    )

    if response.status_code != 200:
        raise ValueError(f"Failed to delete CAS session: {response.text}")


async def get_cas_session_info(
    async_web_session: AsyncClient,
    sas_oauth_token: str,
    base_url: str,
    cas_session_id: str,
) -> SessionModel:
    """
    Get the CAS session info.

    Args:
        async_web_session: The async web session.
        sas_oauth_token: The SAS OAuth token.
        base_url: The base URL.
        cas_session_id: The CAS session ID.

    Returns:
        The CAS session info.
    """
    from ...core.sas.headers import sas_cas_get_session_info_get_headers
    from ...core.sas.url_generators import generate_cas_session_id_url

    response = await async_web_session.get(
        generate_cas_session_id_url(base_url, cas_session_id),
        headers=sas_cas_get_session_info_get_headers(sas_oauth_token),
    )

    if response.status_code != 200:
        raise ValueError(f"Failed to get CAS session info: {response.text}")

    return SessionModel(**response.json())
