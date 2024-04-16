import os
from yt_dlp import YoutubeDL
from google.cloud import storage
from filename_utils import sanitize_filename

def download_audio(video_url, output_path):
    ffmpeg_path = '/usr/bin/ffmpeg'
    """Download the best audio stream and extract as AAC format."""
    output_template = os.path.join(output_path, '%(title)s-%(id)s.%(ext)s')
    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
            'preferredquality': '192',
        }],
        'outtmpl': output_template,
        'merge_output_format': 'aac',  # Ensures the output is in AAC format
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(video_url, download=True)
            original_filepath = ydl.prepare_filename(result)
            filename_only = os.path.basename(original_filepath)
            sanitized_filename = sanitize_filename(filename_only)
            sanitized_filepath = os.path.join(output_path, sanitized_filename)
            os.rename(original_filepath, sanitized_filepath)
            return sanitized_filepath
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def upload_to_gcs(bucket_name, local_file_path, gcs_file_path):
    """Uploads the file to a specified Google Cloud Storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(gcs_file_path)

    blob.upload_from_filename(local_file_path)
    print(f"File {local_file_path} uploaded to GCS bucket '{bucket_name}' at '{gcs_file_path}'")

def main():
    video_url = input("Enter YouTube video URL: ")
    bucket_name = 'all-in-bucket'
    local_output_path = 'downloads'
    gcs_output_path = 'audio/aac'

    os.makedirs(local_output_path, exist_ok=True)  # Ensures the directory exists

    downloaded_file_path = download_audio(video_url, local_output_path)
    if downloaded_file_path:
        gcs_full_path = os.path.join(gcs_output_path, os.path.basename(downloaded_file_path))
        upload_to_gcs(bucket_name, downloaded_file_path, gcs_full_path)

if __name__ == '__main__':
    main()
