"""
YAML configuration parser & loader
"""
from json import load
import yaml
from pathlib import Path

def load_config():
    # get root
    cwd = Path.cwd().resolve()
    config_path = cwd / "config.yaml"

    if not config_path.exists():
        raise FileNotFoundError("cannot find config.yaml")

    with open(config_path, "r") as f:
        file_content = f.read()
        parsed_content = yaml.safe_load(file_content)

    return parsed_content

if __name__ == "__main__":
    try:
        config = load_config()
        print(config)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
