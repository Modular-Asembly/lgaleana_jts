import os
from typing import Any, Dict
from simple_salesforce import Salesforce

def query_salesforce_data(soql_query: str) -> Dict[str, Any]:
    """
    Query data from Salesforce using the provided SOQL query.

    :param soql_query: The SOQL query string to execute.
    :return: The queried data as a dictionary.
    """
    # Step 1: Read Salesforce credentials from environment variables
    sf_username = os.environ["SALESFORCE_USERNAME"]
    sf_password = os.environ["SALESFORCE_PASSWORD"]
    sf_security_token = os.environ["SALESFORCE_SECURITY_TOKEN"]

    # Step 2: Connect to Salesforce authentication endpoint
    sf = Salesforce(
        username=sf_username,
        password=sf_password,
        security_token=sf_security_token
    )

    # Step 3: Use these credentials to connect to Salesforce API
    # Step 4: Query the required data
    result = sf.query(soql_query)

    # Step 5: Return the data
    return result
