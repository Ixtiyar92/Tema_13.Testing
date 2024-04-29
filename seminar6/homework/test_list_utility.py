import pytest
from list_utility import Utility


@pytest.mark.parametrize("list_numbers, expected_result", [
                        pytest.param([1, 2, 3], 2),
                        pytest.param([5, 5, 5, 5, 5], 5),
                        pytest.param([5], 5),
                        pytest.param([], 0)
    ])
def test_get_average(list_numbers, expected_result):
    assert Utility.get_average(list_numbers) == expected_result


@pytest.fixture()
def fill_list(request):
    list1, list2 = request.param
    yield Utility(list1, list2)


@pytest.mark.parametrize("fill_list", [
    ([1, 2, 3], [1, 2, 3]),
    ([2], [2, 2, 2]),
    ([5, 10, 15], [3, 7, 20])
    ], indirect=True)
def test_compare_lists_equality(fill_list):
    assert fill_list.compare_lists() == "Средние значения равны"


@pytest.mark.parametrize("fill_list", [
    ([1, 2, 3], [1, 1, 1]),
    ([3, 2, 1], [1, 1]),
    ([5, 10, 15], [3])
    ], indirect=True)
def test_compare_lists_more(fill_list):
    assert fill_list.compare_lists() == "Первый список имеет большее среднее значение"


@pytest.mark.parametrize("fill_list", [
    ([1, 1, 1], [1, 2, 3]),
    ([1], [2, 2, 2]),
    ([5], [3, 7, 20])
    ], indirect=True)
def test_compare_lists_less(fill_list):
    assert fill_list.compare_lists() == "Второй список имеет большее среднее значение"