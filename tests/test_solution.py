from solutions import user_solution

def test_add():
    assert user_solution.add(2, 3) == 5
    assert user_solution.add(10, 5) == 15

def test_subtract():
    assert user_solution.subtract(10, 5) == 5
    assert user_solution.subtract(20, 4) == 16

