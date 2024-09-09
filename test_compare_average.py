import pytest

from compare_average import List,Comparator


class TestList:

    def test_find_average(self):
        list1 = List([1, 2, 6])
        assert list1.find_average() == 3

        list2 = List([1, 2, 6, 7])
        assert list2.find_average() == 4

        list3 = List([])
        assert list3.find_average() == 0

        list4 = List("notalist")
        with pytest.raises(TypeError):
            assert list4.find_average()

    def test_dummy(self):
        dummy = List([1, 2, 6])
        assert dummy.dummy() is None


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
        assert comparator.dummy() is None
