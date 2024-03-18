

DEBUG = "test"

class test:
    def __init__(self,testeo="hola" ,**kwargs) -> None:
        self.test = "GHola"
        self.testeo = testeo
        print(DEBUG)
        

class Otra(test):
    def __init__(self, **kwargs) -> None:
        super().__init__( **kwargs)
        
        
if __name__ == "__main__":
    print(Otra(testeo="Hola Mundo").testeo)
    