import pytest
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
    my_light.switch(True)
    my_light.switch(False)
    assert(not my_light.is_on)

@pytest.mark.skip
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

@pytest.mark.skip
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
        "type": "on"
        }
        ]
    my_illumination.display_shape(instructions)
    Grid.switch_on.assert_called_once_with(instructions[0]["coords"])

def test_illumination_executes_instructions_toggle(mocker) -> None:
    mocker.patch('main.Grid.toggle')
    my_grid = Grid(1000, 1000)
    my_illumination = Illumination(my_grid)
    instructions = [{
        "coords":  ((887,9), (959,629)),
        "type": "toggle"
        }
        ]
    my_illumination.display_shape(instructions)
    Grid.toggle.assert_called_once_with(instructions[0]["coords"])



def test_illumination_executes_instructions_switch_off(mocker) -> None:
    mocker.patch('main.Grid.switch_off')
    my_grid = Grid(1000, 1000)
    my_illumination = Illumination(my_grid)
    instructions = [{
        "coords":  ((887,9), (959,629)),
        "type": "toggle",
        "toggle": True
        },
        {
        "coords":  ((0, 0), (959,629)),
        "type": "off"
        }
        ]
    my_illumination.display_shape(instructions)
    Grid.switch_off.assert_called_once_with(instructions[1]["coords"])

def test_illumination_executes_instructions_switch_off(mocker) -> None:
    mocker.patch('main.Grid.switch_off')
    my_grid = Grid(1000, 1000)
    my_illumination = Illumination(my_grid)
    instructions = [{
        "coords":  ((887,9), (959,629)),
        "type": "toggle"
        },
        {
        "coords":  ((0, 0), (959,629)),
        "type": "off"}
        ]
    my_illumination.display_shape(instructions)
    Grid.switch_off.assert_called_once_with(instructions[1]["coords"])

def test_grid_can_reset() -> None:
    my_grid = Grid(5, 5)
    my_illumination = Illumination(my_grid)
    instructions = [{
        "coords":  ((0,1), (3,3)),
        "type": "on"
        }
    ]
    my_illumination.display_shape(instructions)
    my_grid.reset()
    assert(my_grid.on_count == 0)

def test_light_starts_with_0_brightness() -> None:
    my_light = Light()
    assert(my_light.brightness == 0)

def test_turn_on_increases_brightness_by_1() -> None:
    my_light = Light()
    my_light.switch(on=True)
    my_light.switch(on=True)
    assert(my_light.brightness == 2)

def test_turn_off_increases_brightness_by_1() -> None:
    my_light = Light()
    my_light.switch(on=True)
    my_light.switch(on=True)
    my_light.switch(on=False)
    assert(my_light.brightness == 1)
