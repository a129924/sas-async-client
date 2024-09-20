from functools import lru_cache


# CAS RESTFul URLs
@lru_cache(maxsize=1)
def generate_cas_base_url(base_url: str) -> str:
    """
    Generate the CAS REST base URL.

    GET:
        - /cas

        Get information about the CAS servers.

    Args:
        base_url (str): The base URL.

    Returns:
        str: The CAS REST base URL.
    """
    return f"{base_url}/cas-shared-default-http/cas"


@lru_cache(maxsize=1)
def generate_cas_sessions_url(base_url: str) -> str:
    """
    Generate the CAS REST sessions URL.

    GET:
        - /cas/sessionList

        Get a list of active sessions. Does not return information that requires connecting to the sessions for retrieval.

    Args:
        base_url (str): The base URL.

    Returns:
        str: The CAS REST sessions URL.

    Schema:
    ```json
        [
            {
                "links": [
                    {
                        "rel": "self",
                        "method": "GET" | "POST" | "PUT" | "DELETE",
                        "href": "{cas_rest_base_url}/cas/sessionList",
                        "uri": "{cas_rest_base_url}/cas/sessionList",
                        "type": "application/json"
                    },
                    ...
                ],
                "uuid": "{uuid}",
                "id": "{id}",
                "name": "{session_name}",
                "user": "{username}",
                "owner": "{username}",
                "state": "connected" | "disconnected"
            },
            ...
        ]
    ```
    """
    return f"{generate_cas_base_url(base_url)}/sessionList"


@lru_cache(maxsize=1)
def generate_cas_session_url(base_url: str) -> str:
    """
    Generate the CAS REST session URL And Post Session ID.

    GET:
        - /cas/sessions

        Get information about the CAS session.

    POST:
        - /cas/sessions

        Create a new CAS session.

    Args:
        base_url (str): The base URL.

    Returns:
        str: The CAS REST session URL And Get Session ID.

    Schema:

        GET:
    ```json
        {
            "links": [
                {
                    "rel": "self",
                    "method": "GET" | "POST" | "PUT" | "DELETE",
                    "href": "{cas_rest_base_url}/cas/sessions",
                    "uri": "{cas_rest_base_url}/cas/sessions",
                    "type": "application/json"
                },
                ...
            ],
            "uuid": "{uuid}",
            "id": "{id}",
            "name": "{session_name}",
            "user": "{username}",
            "owner": "{username}",
            "state": "connected" | "disconnected",
            "provider": "OAuth",
            "activeAction": "{last_finished_action_name}"
            ...
        },
        ...
    ]


    ```
    POST:
    ```json
        {
            "session": "{cas_session_id}"
        }
    ```
    """
    return f"{generate_cas_base_url(base_url)}/sessions"


@lru_cache(maxsize=1)
def generate_cas_session_id_url(base_url: str, cas_session_id: str) -> str:
    """
    Generate the CAS REST session ID URL and delete session.

    Args:
        base_url (str): The base URL.
        cas_session_id (str): The CAS session ID.

    GET:
        - /cas/sessions/{cas_session_id}

        Get information about the CAS session.

    DELETE:
        - /cas/sessions/{cas_session_id}

        Delete a CAS session.

    Returns:
        str: The CAS REST session ID URL.
    """
    return f"{generate_cas_session_url(base_url)}/{cas_session_id}"


def generate_cas_action_url(base_url: str, cas_session_id: str) -> str:
    """
    Generate the CAS REST action URL and shutdown last actions and get all actions info.

    GET:
        - /cas/sessions/{cas_session_id}/actions

        Get information about the All CAS actions.

    DELETE:
        - /cas/sessions/{cas_session_id}/actions

        Cancels the currently running action by sending a cancelAction action.

    Args:
        base_url (str): The base URL.
        cas_session_id (str): The CAS session ID.

    Returns:
        str: The CAS REST action URL.
    """
    return f"{generate_cas_session_id_url(base_url, cas_session_id)}/actions"


def generate_cas_action_name_url(
    base_url: str,
    cas_session_id: str,
    action_name: str,
) -> str:
    """
    Generate the CAS REST action URL and run action.

    GET:
        - /cas/sessions/{cas_session_id}/actions/{action_name}

        Get information about the CAS action.

    POST:
        - /cas/sessions/{cas_session_id}/actions/{action_name}

        Run a new CAS action.

    Args:
        base_url (str): The base URL.
        cas_session_id (str): The CAS session ID.
        action_name (str): The action name.

    Returns:
        str: The CAS REST action URL.
    """

    return f"{generate_cas_action_url(base_url, cas_session_id)}/{action_name}"


# SAS Viya RESTFul URLs
@lru_cache(maxsize=1)
def generate_viya_token_url(base_url: str) -> str:
    """
    Generate the SAS Viya REST And CAS REST OAuth token URL.

    POST:
        - /SASLogon/oauth/token

        Get the SAS Viya RESTFul And CAS RESTFul OAuth token.

    Args:
        base_url (str): The base URL.

    Returns:
        str: The SAS Viya RESTFul And CAS RESTFul OAuth token URL.

    Schema:
    ```json
        {
            "access_token": "{access_token}",
            "token_type": "bearer",
            "expires_in": 43199,
            "scope": "uaa.none",
            "revocable": false,
            "jti": "322fdb2902c84a51a667b90b99fa1f06"
        }
    ```
    """
    return f"{base_url}/SASLogon/oauth/token"
