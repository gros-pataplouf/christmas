from main import Light

def test_light_off_by_default() -> None:
    my_light : Light = Light()
    assert(not my_light.is_on)

def test_light_can_be_switched_on() -> None:
    my_light : Light = Light()
    my_light.switch(True)
    assert(my_light.is_on)