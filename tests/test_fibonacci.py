from src.fibonacci import generateFibonacci
import pytest


def test_fibonacci():
    assert generateFibonacci(3) == [1, 1, 2]
    assert generateFibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert generateFibonacci(2) == [1, 1]
    assert generateFibonacci(1) == [1]
    with pytest.raises(TypeError):
        generateFibonacci("WrongParameterType")
    with pytest.raises(ValueError):
        generateFibonacci(0)
