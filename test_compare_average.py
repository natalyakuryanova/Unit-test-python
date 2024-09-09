import pytest

from compare_average import *


class TestList:

    def test_find_average(self):
        list = List([1, 2, 6])
        assert list.find_average() == 3

        list = List([1, 2, 6, 7])
        assert list.find_average() == 4

        list = List([])
        assert list.find_average() == 0

        list = List("notalist")
        with pytest.raises(TypeError):
            assert list.find_average()

    def test_dummy(self):
        list = List([1, 2, 6])
        assert list.dummy() == None


class TestComparator:

    def test_compare(self):
        comparator = Comparator([1, 2, 6], [1, 2, 6, 7])
        assert comparator.compare() == "Второй список имеет большее среднее значение"

        comparator = Comparator([1, 2, 6, 7], [1, 2, 6])
        assert comparator.compare() == "Первый список имеет большее среднее значение"

        comparator = Comparator([1, 2, 6], [1, 2, 6])
        assert comparator.compare() == "Средние значения равны"

    def test_dummy(self):
        comparator = Comparator([1, 2, 6], [1, 2, 6, 7])
        assert comparator.dummy() == None
