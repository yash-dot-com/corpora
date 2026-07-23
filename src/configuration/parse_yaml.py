"""
this file contains the implementation for YAML parser that
1. reads config.yaml from root 
2. parses the config.yaml 
3. outputs the config object 
"""

import yaml
from src.utils import create_logger as custom_logger

logger = custom_logger.create_custom_logger(__name__)

# create custom logger for YAML parser

def load_config_file():
    """Loads config.yaml file"""
    try:
        with open("config.yaml", "r") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError as e:
        logger.exception("Config file not found: %s", e)
    except Exception as e:
        logger.exception("Failed to load config file: %s", e)

if __name__ == "__main__":
    config = load_config_file()
