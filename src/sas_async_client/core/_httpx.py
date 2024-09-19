from typing import Optional, Union

from httpx import AsyncClient, Limits
from httpx._config import DEFAULT_LIMITS


async def create_async_web_session(
    headers: Optional[dict[str, str]] = None,
    cookies: Optional[dict[str, str]] = None,
    timeout: Union[int, float] = 10,
    verify: bool = False,
    limits: Limits = DEFAULT_LIMITS,
) -> AsyncClient:
    """
    Create an asynchronous HTTP client.

    Args:
        headers (Optional[dict[str, str]], optional): Headers to be sent with the request. Defaults to None.
        cookies (Optional[dict[str, str]], optional): Cookies to be sent with the request. Defaults to None.
        timeout (Union[int, float], optional): Timeout for the request. Defaults to 10.
        verify (bool, optional): Verify the server's SSL certificate. Defaults to False.
        limits (Limits, optional): Limits for the request. Defaults to DEFAULT_LIMITS.

    Returns:
        AsyncClient: An asynchronous HTTP client.

    Example:
        >>> async with create_async_web_session() as client:
        >>>     response = await client.get("https://example.com")
        >>>     print(response.text)
    """
    return AsyncClient(
        headers=headers,
        cookies=cookies,
        timeout=timeout,
        verify=verify,
        limits=limits,
    )
