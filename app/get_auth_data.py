import os
import requests
from typing import Dict, Any

def get_auth_data() -> Dict[str, Any]:
    auth_url = 'https://login.salesforce.com/services/oauth2/token'
    
    auth_data = {
        'grant_type': 'password',
        'client_id': os.environ['SALESFORCE_CLIENT_ID'],
        'client_secret': os.environ['SALESFORCE_CLIENT_SECRET'],
        'username': os.environ['SALESFORCE_USERNAME'],
        'password': os.environ['SALESFORCE_PASSWORD']
    }
    
    response = requests.post(auth_url, data=auth_data)
    response.raise_for_status()  # Raise an error for bad responses
    
    return response.json()
