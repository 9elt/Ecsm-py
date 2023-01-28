import json

from src.compiler import live_compiler
from src.setup import setup_project

def main():

    try:
        with open("ecsm.config.json", "r") as json_config:
            config = json.load(json_config)
            name = config["name"]
            print(f"\n\x1b[1m\x1b[33m[{name}]\x1b[0m\x1b[1m auto compiler\x1b[0m running...")
    except:
        setup_project()

    live_compiler()

if __name__ ==  "__main__":
    main()