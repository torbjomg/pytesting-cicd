from pytesting_cicd import script


def test_script():
    assert script.run_functions(1, 2, 3) == 0
    assert script.run_functions(0, 0, 0) == 0
    assert script.run_functions(-1, -1, -1) == 0
    assert script.run_functions(1, -1, 0) == 0
