import json
import boto3

def load_config(file_path):
    """
    Load configuration from a JSON file.

    :param file_path: Path to the JSON configuration file.
    :return: Dictionary containing the configuration data.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Configuration file '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file '{file_path}'.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while loading the configuration: {e}")
        return {}

def start_boto3_session(config, key, default=None):
    """
    Create and return a boto3 Session using credentials from a configuration dictionary.

    Args:
        config (dict): The configuration dictionary containing AWS credentials and region.
        key (str): The key in the config dict where AWS credentials and region are stored.
        default (Any, optional): The default value to use if a credential or region is missing. Defaults to None.

    Returns:
        boto3.Session: An authenticated boto3 Session object for further AWS operations.
    """
    access_key = config.get(key, {}).get("AWS_ACCESS_KEY", default)
    secret_key = config.get(key, {}).get("AWS_SECRET_KEY", default)
    region = config.get(key, {}).get("AWS_REGION", default)

    boto3_session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    return boto3_session
