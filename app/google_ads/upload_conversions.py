import os
import requests
from datetime import datetime
from typing import List, Dict, Any

from app.google_ads.get_oauth_token import get_oauth_token


def upload_conversions(records: List[Dict[str, Any]]) -> Any:
    action_id = 462477827
    customer_id = os.environ["GADS_CUSTOMER"]
    api_version = "v18"

    access_token = get_oauth_token()

    url = f"https://googleads.googleapis.com/{api_version}/customers/{customer_id}:uploadClickConversions"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "developer-token": os.environ["GADS_DEVELOPER_TOKEN"],
        "login-customer-id": os.environ["GADS_LOGIN_CUSTOMER_ID"],
    }
    payload = {
        "conversions": [
            {
                "conversionAction": f"customers/{customer_id}/conversionActions/{action_id}",
                "gclid": record["GCLID__c"],
                "conversionValue": 1.0,
                "conversionDateTime": datetime.strptime(
                    record["CreatedDate"], "%Y-%m-%dT%H:%M:%S.%f%z"
                ).strftime("%Y-%m-%d %H:%M:%S%z"),
                "currencyCode": "USD",
            }
            for record in records
        ],
        "partialFailure": True,
        "validateOnly": False,
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
