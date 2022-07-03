import pytest

from src.eight_queen.eight_queen_puzzle import get_number_of_solutions

data: list = [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
    (10, 724)
]


@pytest.mark.parametrize("number,number_of_solutions", data)
def test_get_number_of_solutions_1(number: int, number_of_solutions: int):
    assert get_number_of_solutions(number) == number_of_solutions
