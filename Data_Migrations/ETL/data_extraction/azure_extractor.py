# azure_extractor.py
from azure.storage.blob import BlobServiceClient


def extract_data(connection_string, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    extracted_data = []
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob.name)
        data = blob_client.download_blob().readall()
        extracted_data.append(data)

    return extracted_data

# Similarly, create similar functions in google_extractor.py and dropbox_extractor.py
