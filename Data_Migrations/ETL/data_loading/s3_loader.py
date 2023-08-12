import boto3


def load_data_to_s3(aws_access_key_id, aws_secret_access_key, aws_region, s3_bucket_name, data, file_name):
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                             region_name=aws_region)

    s3_client.put_object(Body=data, Bucket=s3_bucket_name, Key=file_name)
