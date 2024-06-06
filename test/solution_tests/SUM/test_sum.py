import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

# test sum with a negative integer returns an error
    def test_sum_negative_integer_returns_an_error(self):
        with pytest.raises(Exception) as e_info:
            sum_solution.compute(-100, -100)

    def test_sum_integer_greater_than_zero_raises_exception(self):
        with pytest.raises(Exception) as e_info:
            sum_solution.compute(101, 101)




