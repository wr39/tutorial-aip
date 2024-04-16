from google.cloud import storage
import os

def upload_files_to_gcs(bucket_name, source_folder, destination_blob_prefix):
    """Uploads all files from a local folder to a GCS bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for file_name in os.listdir(source_folder):
        local_path = os.path.join(source_folder, file_name)
        if os.path.isfile(local_path):  # Make sure it's a file
            blob_path = os.path.join(destination_blob_prefix, file_name)
            blob = bucket.blob(blob_path)
            blob.upload_from_filename(local_path)
            print(f"Uploaded {local_path} to gs://{bucket_name}/{blob_path}")

# Example usage
upload_files_to_gcs('all-in-bucket', '/home/wilson_robert_39/downloads', 'audio/aac')
