import pytest
from factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial(-1)

def test_factorial_large():
    # Test a larger number, but keep it reasonable
    assert factorial(20) == 2432902008176640000