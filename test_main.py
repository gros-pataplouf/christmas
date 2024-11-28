from main import Light

def test_light_off_by_default() -> None:
    my_light : Light = Light()
    assert(not my_light.is_on)