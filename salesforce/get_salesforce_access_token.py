import os
from typing import Dict
import requests

def get_salesforce_access_token() -> Dict[str, str]:
    """
    Connects to the Salesforce authentication endpoint to obtain an access token and instance URL.

    Returns:
        Dict[str, str]: A dictionary containing the access token and instance URL.
    """
    # Retrieve Salesforce credentials from environment variables
    client_id = os.environ['SALESFORCE_CLIENT_ID']
    client_secret = os.environ['SALESFORCE_CLIENT_SECRET']
    username = os.environ['SALESFORCE_USERNAME']
    password = os.environ['SALESFORCE_PASSWORD']
    security_token = os.environ['SALESFORCE_SECURITY_TOKEN']

    # Salesforce authentication endpoint
    auth_url = "https://login.salesforce.com/services/oauth2/token"

    # Prepare the payload for the POST request
    payload = {
        'grant_type': 'password',
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': f"{password}{security_token}"
    }

    # Make the POST request to obtain the access token
    response = requests.post(auth_url, data=payload)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the JSON response
    auth_response = response.json()

    # Extract the access token and instance URL
    access_token = auth_response['access_token']
    instance_url = auth_response['instance_url']

    return {
        'access_token': access_token,
        'instance_url': instance_url
    }
