
from core.core import read_csv ,import_json_default as  load
class Configuration:
    def __init__(self) -> None:
        content = load("data/configuration.json")
        self.__display = content.get("Display")
        try:
            self.debug = self.__display.get("DebugMode")
            self.__key_language = self.__display.get("Language")
            self.resolution = self.__display.get("Resolution").split("x")
            self.language = self.__configure_language()
            
        except Exception as err:
            print("Error load configuration")
        
            
    def __configure_language(self):
        data = read_csv("data/language/language.csv")
        content = data.get("data")
        header = data.get("header")
        new_data = {}
        for head in header:
            head_content = head.split(";")
            for index in range(0, len(head_content)):
                new_data.update({head_content[index]:{} })
                for elements_content in content:
                    content_data = elements_content[0].split(";")
                    for index_content in range(0,len(content_data)):
                        new_data[head_content[index]].update({content_data[0]:content_data[index_content]})
                    
            
        return new_data
                    
        
    