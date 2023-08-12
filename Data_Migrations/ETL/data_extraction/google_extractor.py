from azure.storage.blob import BlobServiceClient
from google.cloud import storage
import dropbox
def extract_google_data(project_id, bucket_name):
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(bucket_name)

    extracted_data = []
    for blob in bucket.list_blobs():
        data = blob.download_as_text()
        extracted_data.append(data)

    return extracted_data

