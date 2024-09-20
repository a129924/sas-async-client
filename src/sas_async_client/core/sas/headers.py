from functools import lru_cache


def sas_access_token_headers() -> dict[str, str]:
    """
    Returns the headers for the SAS access token request.
    """
    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic c2FzLmNsaTo=",
    }


@lru_cache(maxsize=10)
def sas_viya_table_get_headers(access_token: str) -> dict[str, str]:
    """
    Returns the headers for the SAS Viya table GET request.
    """
    return {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.sas.data.table+json, application/vnd.sas.data.table.summary+json, application/json",
    }


@lru_cache(maxsize=10)
def sas_cas_get_session_id_post_headers(access_token: str) -> dict[str, str]:
    """
    Returns the headers for the SAS CAS GET session ID POST request.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json, application/vnd.sas.cas.direct.session.id, application/vnd.sas.cas.direct.error.response",
    }


@lru_cache(maxsize=10)
def sas_cas_action_get_headers(access_token: str) -> dict[str, str]:
    """
    Returns the headers for the SAS CAS action GET request.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        # "Accept": "application/json, application/vnd.sas.cas.direct.action.list, application/vnd.sas.cas.direct.error.response",
        "Accept": "application/vnd.sas.cas.direct.action.definition",
    }


@lru_cache(maxsize=10)
def sas_cas_action_post_headers(access_token: str) -> dict[str, str]:
    """
    Returns the headers for the SAS CAS action POST request.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json, application/vnd.sas.cas.direct.action.results, application/vnd.sas.cas.direct.error.response",
    }
