import os
from typing import Tuple
from simple_salesforce import Salesforce

def get_salesforce_access_token() -> Tuple[str, str]:
    # Retrieve Salesforce credentials from environment variables
    username = os.environ["SALESFORCE_USERNAME"]
    password = os.environ["SALESFORCE_PASSWORD"]
    security_token = os.environ["SALESFORCE_SECURITY_TOKEN"]
    domain = os.environ.get("SALESFORCE_DOMAIN", "login")  # Default to 'login' if not specified

    # Connect to Salesforce
    sf = Salesforce(
        username=username,
        password=password,
        security_token=security_token,
        domain=domain
    )

    # Return the access token and instance URL
    return sf.session_id, sf.sf_instance
