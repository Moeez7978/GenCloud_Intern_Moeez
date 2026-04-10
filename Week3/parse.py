import json
import sys
import os

CONFIG_FILE = "config.json"

def validate_config(config):
    errors = []

    # Required fields
    required_fields = ["host", "port"]

    for field in required_fields:
        if field not in config:
            errors.append(f"Missing required field: {field}")

    # Type checks
    if "port" in config and not isinstance(config["port"], int):
        errors.append("Port must be an integer")

    if "debug" in config and not isinstance(config["debug"], bool):
        errors.append("Debug must be true/false")

    # Value checks
    if "port" in config:
        if not (1 <= config["port"] <= 65535):
            errors.append("Port must be between 1 and 65535")

    if "max_connections" in config:
        if config["max_connections"] <= 0:
            errors.append("max_connections must be > 0")

    return errors


def main():
    # Check file exists
    if not os.path.exists(CONFIG_FILE):
        print("Config file not found!")
        sys.exit(1)

    # Load config
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    except json.JSONDecodeError:
        print("Invalid JSON format!")
        sys.exit(1)

    # Validate
    errors = validate_config(config)

    if errors:
        print("Configuration Errors:")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)
    else:
        print("Configuration is valid!")


if __name__ == "__main__":
    main()
