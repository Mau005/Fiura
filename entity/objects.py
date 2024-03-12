
class ObjectIntenal:
    def __init__(self, payload:dict) -> None:
        self.TypeFlag = payload.get("TypeFlag")
        self.NameSprite = payload.get("NameSprite")
        self.Sprites = payload.get("Sprites")
        self.Animation = payload.get("Animation")
        self.AnimatedSequence = tuple(payload.get("AnimatedSequence"))
    def __str__(self) -> str:
        return '''
        self.TypeFlag = {}
        self.NameSprite = {}
        self.Sprites = {}
        self.Animation = {}
        self.AnimatedSequence = {}
    
    '''.format(self.TypeFlag, self.NameSprite, self.Sprites, self.Animation, self.AnimatedSequence)
        
class ItemsInternal:
    def __init__(self, payload:dict) -> None:
        self.Name = payload.get("Name")
        self.Description =  payload.get("Description")
        self.DataFactory =  payload.get("DataFactory")
        self.__ObjectIntenal = None
        
    def __str__(self) -> str:
        return '''
Name: {}
Description: {}
ObjectInternal: {}
    '''.format(self.Name, self.Description, self.__ObjectIntenal)
        
    @property
    def object_internal(self):
        return self.__ObjectIntenal
    
    @object_internal.setter
    def object_internal(self, obj:ObjectIntenal):
        self.__ObjectIntenal = obj
        
    