# filename_utils.py
import re

def sanitize_filename(filename):
    """
    Sanitizes the filename by removing or replacing characters that might not be supported
    by the file system or cloud services.

    Parameters:
    - filename (str): The original filename.

    Returns:
    - str: The sanitized filename.
    """
    # Replace spaces and non-ASCII characters with a single hyphen
    sanitized = re.sub(r'[ \u0080-\uFFFF]', '-', filename)
    # Replace sets of problematic filesystem characters with a single hyphen
    sanitized = re.sub(r'[\\/*?:"<>|\']+','-', sanitized)
    return sanitized
