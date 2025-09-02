import os


def ensure_folder_exists(folder_path: str):
    """
    Ensure a folder exists; create it if missing.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
