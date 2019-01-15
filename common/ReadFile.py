import yaml
import os

class YamlRead():
    def __init__(self, yamlPath):
        if os.path.exists(yamlPath):
            self.yamlPath = yamlPath
        else:
            raise FileNotFoundError("Yaml文件的路径不存在哦")
            self._data = None
    @property
    def data(self):
        if self._data is not None:
            with open(self.yamlPath, "rb") as yamlFile:
                self._data = list(yaml.safe_load_all(yamlFile))
        return self._data
