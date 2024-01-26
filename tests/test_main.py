import pytest
from decimal import Decimal

from backend.main import calculate_factorial, factorial_cache


class TestCalculateFactorial():
    def test_factorial_positive(self):
        # Test with positive integers
        assert calculate_factorial(0) == Decimal(1)
        assert calculate_factorial(5) == Decimal(120)
        assert calculate_factorial(10) == Decimal(3628800)

    def test_factorial_negative(self):
        # Test with negative integer
        assert not calculate_factorial(-5)

    def test_factorial_cache(self):
        # Test if caching is working
        global factorial_cache
        assert calculate_factorial(5) == Decimal(120)
        assert 5 in factorial_cache
        assert factorial_cache.get(5) == 120
        assert factorial_cache[5] == Decimal(120)