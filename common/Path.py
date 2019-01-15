import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_YAML_PATH = os.path.join(BASE_PATH, "config", "config.yaml")
DRIVERS_PATH = os.path.join(BASE_PATH, "drivers")


