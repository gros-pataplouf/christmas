class Light():
    def __init__(self):
        self.__is_on = False
    
    @property
    def is_on(self):
        return self.__is_on
    
    def switch(self, on=None):
        self.__is_on = on if on is not None else not self.__is_on

class Grid():
    def __init__(self, width : int, height : int):
        self.matrix = [[Light() for elt in range(0, width)] for elt in range(0, height)]

    
    def switch(self, coords: tuple, on=False, toggle=False):
        (p1, p2) = coords
        (x1, y1) = p1
        (x2, y2) = p2
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if not toggle:
                    self.matrix[i][j].switch(on)
                else:
                    self.matrix[i][j].switch()

    
    def switch_on(self, coords : tuple):
        self.switch(coords, on=True)


    def switch_off(self, coords : tuple):
        self.switch(coords, on=False)


    def toggle(self, coords : tuple):
        self.switch(coords, toggle=True)
