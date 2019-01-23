import os
import logging
from common.ReadFile import YamlRead
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_YAML_PATH = os.path.join(BASE_PATH, "config", "config.yaml")
DRIVERS_PATH = os.path.join(BASE_PATH, "drivers")
REPORT_PATH = os.path.join(BASE_PATH,"report")
LOG_PATH = os.path.join(BASE_PATH,"log")

class Config():
    def __init__(self, config = CONFIG_YAML_PATH):
        logging.warning("YAML配置文件的地址为"+config)
        self.config =YamlRead(config).data
    def get(self, element, index = 0):
        return self.config[index].get(element)
