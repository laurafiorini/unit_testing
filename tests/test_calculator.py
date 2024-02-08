import pytest
from calculator.calculate import calculate

case_tests = [(5, 2, '**', 25),
              (8, 4, '-', 4),
              (3, 3, '^', 27),
              (4, 6, '*', 24),
              (7, 8, 'x', 56),
              (9, 3, '/', 3),
              (1, 6, '+', 7)]

@pytest.mark.parametrize("num1, num2, operator, result", case_tests)
def test_calculate_cases(num1, num2, operator, result):
    assert calculate(num1, num2, operator) == result

error_tests = [(1, 2, '%'),
               ('1', 2, '+'),
               (1, '2', '+'),
               ('1', '2', '+')]

@pytest.mark.parametrize("num1, num2, operator", error_tests)
def test_calculate_errors(num1, num2, operator):
    with pytest.raises(ValueError):
        calculate(num1, num2, operator)