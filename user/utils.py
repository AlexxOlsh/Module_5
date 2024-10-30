from django.conf import settings
from requests_oauthlib import OAuth2Session


def github_setup(redirect_uri: str):
    session = OAuth2Session(settings.GITHUB_CLIENT_ID, redirect_uri=redirect_uri)
    authorization_url, _ = session.authorization_url(settings.GITHUB_AUTH_URL)

    return authorization_url


def github_callback(redirect_uri: str, auth_uri: str):
    session = OAuth2Session(settings.GITHUB_CLIENT_ID, redirect_uri=redirect_uri)

    session.fetch_token(
        settings.GITHUB_TOKEN_URL,
        client_secret=settings.GITHUB_CLIENT_SECRET,
        authorization_response=auth_uri,
    )

    user_data = session.get("https://api.github.com/user").json()
    return user_data