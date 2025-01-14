from typing import List, Dict, Any
from simple_salesforce import Salesforce
from salesforce.get_salesforce_access_token import get_salesforce_access_token

def query_salesforce_data() -> List[Dict[str, Any]]:
    """
    Queries Salesforce data using the access token and instance URL obtained from Salesforce.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing the queried Salesforce data.
    """
    # Obtain Salesforce credentials
    credentials = get_salesforce_access_token()
    access_token = credentials['access_token']
    instance_url = credentials['instance_url']

    # Connect to Salesforce using the simple-salesforce library
    sf = Salesforce(instance_url=instance_url, session_id=access_token)

    # Define the SOQL query to retrieve the required data
    soql_query = "SELECT Id, Name FROM Account LIMIT 10"  # Example query

    # Execute the query
    query_result = sf.query(soql_query)

    # Extract the records from the query result
    records = query_result['records']

    return records
