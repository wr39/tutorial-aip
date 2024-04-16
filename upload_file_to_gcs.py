## WORK ON SANITIZING FILENAME

from google.cloud import storage
import os

def upload_file_to_gcs(bucket_name, local_file_path, destination_blob_path):
    """Uploads a specific file to a GCS bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_path)

    # Upload the file
    blob.upload_from_filename(local_file_path)
    print(f"Uploaded {local_file_path} to gs://{bucket_name}/{destination_blob_path}")

# Example usage
bucket_name = 'all-in-bucket'  # Replace with your actual bucket name
local_file_path = '/home/wilson_robert_39/downloads/E167： Google's Woke AI disaster, Nvidia smashes earnings (again), Groq's LPU breakthrough & more-z6vrKA_L5pk.m4a'  # Adjust the path as needed
destination_blob_path = 'audio/aac'  # Destination path in GCS

upload_file_to_gcs(bucket_name, local_file_path, destination_blob_path)
