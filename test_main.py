from main import Light, Grid, Illumination

def test_light_off_by_default() -> None:
    my_light : Light = Light()
    assert(not my_light.is_on)

def test_light_can_be_switched_on() -> None:
    my_light : Light = Light()
    my_light.switch(True)
    assert(my_light.is_on)

def test_light_can_be_switched_off() -> None:
    my_light : Light = Light()
    my_light.switch(False)
    assert(not my_light.is_on)

def test_light_can_be_toggled() -> None:
    my_light : Light = Light()
    my_light.switch()
    assert(my_light.is_on)
    my_light.switch()
    assert(not my_light.is_on)

def test_1000x1000_grid_consists_of_lights() -> None:
    my_grid : Grid = Grid(1000, 1000)
    assert(len(my_grid.matrix) == 1000)
    assert(len(my_grid.matrix[0]) == 1000)
    assert(isinstance(my_grid.matrix[0][0], Light))

def test_lights_in_grid_switched_on_by_coords() -> None:
    my_grid : Grid = Grid(1000, 1000)
    x1 : int = 0
    y1 : int = 4
    x2 : int = 5
    y2 : int = 9
    my_grid.switch_on(((x1, y1), (x2, y2)))
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            assert(my_grid.matrix[i][j].is_on)

def test_lights_in_grid_switched_off_by_coords() -> None:
    my_grid : Grid = Grid(1000, 1000)
    x1 : int = 0
    y1 : int = 4
    x2 : int = 5
    y2 : int = 9
    my_grid.switch_on(((x1, y1), (x2, y2)))
    my_grid.switch_off(((x1, y1), (x2, y2)))
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            assert(not my_grid.matrix[i][j].is_on)

def test_lights_in_grid_toggled_by_coords() -> None:
    my_grid : Grid = Grid(4, 4)
    x1 : int = 0
    y1 : int = 0
    x2 : int = 2
    y2 : int = 2
    x3 : int = 3
    y3 : int = 3
    my_grid.switch_on(((x1, y1), (x2, y2)))
    my_grid.toggle(((x1, y1), (x3, y3))) #toggle the whole grid
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            assert(not my_grid.matrix[i][j].is_on)
    assert(my_grid.matrix[3][3].is_on)

def test_lights_in_grid_switched_off_by_coords() -> None:
    my_grid : Grid = Grid(1000, 1000)
    x1 : int = 0
    y1 : int = 0
    x2 : int = 4
    y2 : int = 4
    my_grid.switch_on(((x1, y1), (x2, y2)))
    assert(my_grid.on_count == 25)
    my_grid.toggle(((0, 0), (999, 999)))
    assert(my_grid.on_count == 999975)

def test_illumination_executes_instructions(mocker) -> None:
    mocker.patch('main.Grid.switch_on')
    my_grid = Grid(1000, 1000)
    my_illumination = Illumination(my_grid)
    instructions = [{
        "coords":  ((887,9), (959,629)),
        "on": True,
        "toggle": False
        }
        ]
    my_illumination.illuminate(instructions)
    Grid.switch_on.assert_called_once_with(instructions[0]["coords"])

def test_illumination_executes_instructions_toggle(mocker) -> None:
    mocker.patch('main.Grid.toggle')
    #mocker.patch('main.Grid.switch_off')
    my_grid = Grid(1000, 1000)
    my_illumination = Illumination(my_grid)
    instructions = [{
        "coords":  ((887,9), (959,629)),
        "on": False,
        "toggle": True
        },
        {
        "coords":  ((0, 0), (959,629)),
        "on": False,
        "toggle": False
        }
        ]
    my_illumination.illuminate(instructions)
    Grid.toggle.assert_called_once_with(instructions[0]["coords"])
    #Grid.switch_off.toggle.assert_called_once_with(instructions[1]["coords"])



