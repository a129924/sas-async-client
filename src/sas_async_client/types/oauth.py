from datetime import datetime, timedelta

from pydantic import BaseModel, computed_field


class OAuthToken(BaseModel):
    access_token: str
    token_type: str
    id_token: str
    refresh_token: str
    expires_in: int
    scope: str
    jti: str

    @computed_field
    @classmethod
    def expires_at(cls) -> datetime:
        """
        Returns the expiration time of the token.
        """
        return datetime.now() + timedelta(seconds=cls.expires_in - 10)
