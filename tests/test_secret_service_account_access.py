from google.cloud import secretmanager

def access_secret_version(project_id, secret_id, version_id="latest"):
    """
    Access a secret version in Google Secret Manager.

    Parameters:
    - project_id (str): The GCP project ID where the secret is managed.
    - secret_id (str): The ID of the secret within the Secret Manager.
    - version_id (str): The version of the secret (default is "latest").

    Returns:
    - str: The content of the secret as a string.
    """
    # Create a client to connect to the Secret Manager API
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version
    response = client.access_secret_version(request={"name": name})

    # Extract the secret payload as a string (assuming it's stored in UTF-8 encoding)
    secret_string = response.payload.data.decode('UTF-8')

    return secret_string

# Usage example
project_id = "all-in-project-420308"
secret_id = "gcs-uploader-prod-service-account"
secret_content = access_secret_version(project_id, secret_id)
print("Retrieved secret content:", secret_content)
