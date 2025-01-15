import os
import requests


def get_oauth_token() -> str:
    token_url = "https://www.googleapis.com/oauth2/v3/token"
    client_id = os.environ["GADS_CLIENT_ID"]
    client_secret = os.environ["GADS_CLIENT_SECRET"]
    refresh_token = os.environ["GADS_REFRESH_TOKEN"]
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
    }

    response = requests.post(token_url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]
