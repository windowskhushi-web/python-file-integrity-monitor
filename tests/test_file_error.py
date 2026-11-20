
from src.hash_generator import calculate_sha256

try:
    calculate_sha256("monitored_files/nonexistent.txt")
except FileNotFoundError as error:
    print("File error handled successfully:", error)
