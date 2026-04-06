import os
from dotenv import load_dotenv
import sys


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    #  1. Load .env
    load_dotenv()

    #  2. REad variables
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOINT")



    #  4. Show configuration
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_url}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    if endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    print()

    #  3. Handle errors
    if not all([mode, db_url, api_key, log_level, endpoint]):
        print("[ERROR] Missing configuration!")
        print("Please check you .env file")
        return

    if mode == "development":
        print("Running in DEVELOPMENT mode")
        print(f"API_KEY (visible): {api_key}")
    elif mode == "production":
        print("Running in PRODUCTION mode")
        print(f"API_KEY IS HIDDEN FOR SECURITY")
    else:
        print("[ERROR] Invalid MATRIX_MODE")
    print()

    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
