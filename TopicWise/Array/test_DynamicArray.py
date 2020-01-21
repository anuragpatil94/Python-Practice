import pytest
from TopicWise.Array.DynamicArray import DynamicArray


class TestDynamicArray:
    def test_insert(self):
        array = DynamicArray(5)
        array.push(5)
        assert array[0] == 5

    def test_len(self):
        array = DynamicArray(5)
        arr = [1, 2, 3, 4, 5]
        for num in arr:
            array.push(num)
        assert len(array) == 5

    def test_resize(self):
        array = DynamicArray(5)
        arr = [1, 2, 3, 4, 5, 6]
        for num in arr:
            array.push(num)
        assert len(array) == 6
        assert array.currentCapacity() == 10
