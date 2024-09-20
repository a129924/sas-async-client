from httpx import AsyncClient

from ...types.oauth import OAuthToken
from .headers import sas_access_token_headers


async def get_sas_access_token(
    async_web_session: AsyncClient,
    base_url: str,
    user_id: str,
    user_password: str,
    headers: dict[str, str] = sas_access_token_headers(),
) -> OAuthToken:
    """
    Get the SAS access token.

    Args:
        async_web_session: The async web session.
        base_url: The base URL.
        user_id: The user ID.
        user_password: The user password.
        headers: The headers.

    Returns:
        The SAS access token.

    Raises:
        ValueError: If the SAS access token is not found.

    Example:
        >>> async_web_session = create_async_web_session()
        >>> access_token = await get_sas_access_token(async_web_session, "https://your-sas-server.com", "your-user-id", "your-user-password")
    """
    response = await async_web_session.post(
        f"{base_url}/SASLogon/oauth/token",
        headers=headers,
        data={
            "grant_type": "password",
            "username": user_id,
            "password": user_password,
        },
    )

    if response.status_code != 200:
        raise ValueError(f"Failed to get SAS access token: {response.text}")

    return OAuthToken(**response.json())
