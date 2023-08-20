# azure_extractor.py
from azure.storage.blob import BlobServiceClient


def extract_data(connection_string, container_name):
    """
       Extracts data from blobs within an Azure Blob Storage container.

       Args:
           connection_string (str): The connection string for accessing the Azure Blob Storage.
           container_name (str): The name of the container within the Blob Storage.

       Returns:
           list: A list containing the extracted data from each blob within the container.

        Developer: Pratik Domadiya
        Team: Cloud Data Extraction Team
       """


    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    extracted_data = []
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob.name)
        data = blob_client.download_blob().readall()
        extracted_data.append(data)

    return extracted_data

# Similarly, create similar functions in google_extractor.py and dropbox_extractor.py
