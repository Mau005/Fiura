
from core.core import import_json_default as load
class Configuration:
    def __init__(self) -> None:
        content = load("data/configuration.json")
        self.__display = content.get("Display")
        try:
            self.debug = self.__display.get("DebugMode")
            self.__key_language = self.__display.get("Language")
            self.resolution = self.__display.get("Resolution").split("x")
            print(self.resolution)
        except Exception as err:
            print("Error load configuration")
            