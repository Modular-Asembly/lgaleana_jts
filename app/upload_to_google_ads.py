from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException
from typing import Dict, Any

def upload_to_google_ads(formatted_data: Dict[str, Any]) -> None:
    """
    Uploads a campaign to Google Ads using the provided formatted data.

    Args:
        formatted_data (Dict[str, Any]): The data formatted for Google Ads, including campaign details.
    """
    # Initialize the Google Ads client
    client = GoogleAdsClient.load_from_storage()

    # Get the CampaignService client
    campaign_service = client.get_service("CampaignService")

    # Create a campaign operation
    campaign_operation = client.get_type("CampaignOperation")
    campaign = campaign_operation.create

    # Set campaign details from formatted_data
    campaign.name = formatted_data["name"]
    campaign.advertising_channel_type = formatted_data["advertising_channel_type"]
    campaign.status = formatted_data["status"]

    # Send the campaign operation to the Google Ads API
    try:
        response = campaign_service.mutate_campaigns(
            customer_id=formatted_data["customer_id"],
            operations=[campaign_operation]
        )
        print(f"Created campaign with resource name: {response.results[0].resource_name}")
    except GoogleAdsException as ex:
        print(f"Request with ID '{ex.request_id}' failed with status '{ex.error.code().name}' and includes the following errors:")
        for error in ex.failure.errors:
            print(f"\tError with message '{error.message}'.")
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")

