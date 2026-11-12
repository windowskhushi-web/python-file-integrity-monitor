
import hashlib


def calculate_sha256(file_path):
    """
    Calculate the SHA-256 hash of a file.

    Args:
        file_path: Path to the file.

    Returns:
        SHA-256 hash as a hexadecimal string.
    """

    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            hasher.update(chunk)

    result = hasher.hexdigest()

    return result
