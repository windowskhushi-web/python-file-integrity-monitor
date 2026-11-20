
from pathlib import Path


def scan_directory(directory_path):
    """
    Scan a directory and return paths of all files.

    Args:
        directory_path: Directory to scan.

    Returns:
        List of file paths.
    """

    directory = Path(directory_path)

    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory_path}")

    files = []

    for item in directory.rglob("*"):
        if item.is_file():
            files.append(item)

    return files
