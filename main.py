class Light():
    def __init__(self):
        self.__is_on = False
    
    @property
    def is_on(self):
        return self.__is_on
    
    def switch(self, on):
        self.__is_on = on