import pytest


@pytest.fixture(autouse=True)
def resource_setup():
    print("resource_setup")
    yield
    print("resource_teardown")
#
#
# def test_3_that_does_again(resource_setup):
#     print("test_3_that_does_again")
#     print(5 + 2)
#     assert 5 == 6
#
# def test_1_check_number(x):
#     return x + 1
#
# def test_2_check():
#     assert test_1_check_number(5) - 3 == 10
# # @pytest.mark.parametrize("x", [1,2])
# # @pytest.mark.parametrize("y", [10,11])
# # def test_cross_params(x, y):
# #     print("x: {0}, y: {1}".format(x, y))
# #     assert True
#
#
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#    assert eval(test_input) == expected


@pytest.mark.parametrize("a, expected", [(5, 5), (7, 9), (8, 7), (9, 9)])
def test_check_varibles(a, expected):
    assert a == expected, "a =! b please check"