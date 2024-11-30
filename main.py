from instructions import INSTRUCTIONS

class Light():
    def __init__(self):
        self.__is_on = False
        self.__brightness = 0
    
    @property
    def is_on(self):
        return self.__is_on
    
    @property
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, added_brightness):
        self.__brightness = self.__brightness + added_brightness
        if self.__brightness < 0:
            self.__brightness = 0

    def switch(self, on=None):
        if on is None:
            self.brightness = 2
        elif on == False:
            self.brightness = -1
        else:
            self.brightness = 1
        self.__is_on = True if self.brightness > 0 else False

class Grid():
    
    def __init__(self, width : int, height : int):
        self.matrix = [[Light() for elt in range(0, width)] for elt in range(0, height)]
        self.__width = width
        self.__height = height
        self.__on_count = 0

    def __str__(self):

        def map_brightness(value):
            if value == 0:
                return " "
            elif value == 1:
                return "*"
            else:
                return "O"

        return "".join(
            list(
                map(
                    lambda row: "".join(
                        list(
                            map(
                                lambda elt : map_brightness(elt.brightness), row))) + "\n", self.matrix)))

    @property
    def on_count(self):
        return self.__on_count
    
    def update_on_count(self, light: Light, on: bool, toggle: bool):
        is_on = light.is_on
        if toggle:
            self.__on_count = self.__on_count + 1 if not is_on else self.__on_count - 1
        elif is_on == on:
            pass
        else:
            self.__on_count = self.__on_count + 1 if on else self.__on_count - 1

  
    def switch(self, coords: tuple, on=False, toggle=False):
        (p1, p2) = coords
        (x1, y1) = p1
        (x2, y2) = p2
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                self.update_on_count(self.matrix[i][j], on, toggle)
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
    
    def reset(self):
        self.switch_off(((0, 0), (self.__width -1, self.__height - 1)))

    
class Illumination():
    
    def __init__(self, grid : Grid):
        self.grid = grid
    
    def display_shape(self, instruction):
        for i in instruction:
            match i["type"]:
                case "toggle":
                    self.grid.toggle(i["coords"])
                case "on":
                    self.grid.switch_on(i["coords"])
                case "off":
                    self.grid.switch_off(i["coords"])

    
    def lightshow(self, instructions : list = INSTRUCTIONS):
        for i in instructions:
            self.display_shape(i)
            print(self.grid)
            self.grid.reset()


if __name__ == "__main__":
    grid = Grid(50, 25)
    illumination = Illumination(grid)
    illumination.lightshow()
