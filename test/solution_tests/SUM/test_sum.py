import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

# test sum with a negative integer returns an error
    def test_sum_negative_integer_returns_an_error(self):
        pytest.raises()
# test sum at the boundary of 0 and 100


