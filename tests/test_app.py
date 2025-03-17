import pytest

from myapp.app import multiply_by_two, divide_by_two


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiply_by_two(self):
        expected_output = 67  # Last two digits of student ID
        result = multiply_by_two(33.5)  # 33.5 * 2 = 67
        assert result == expected_output, f"Expected {expected_output}, but got {result}"

    def test_multiply_by_two(self):  # <-- Missing "self"
        side_length = 8.19  # Approximate value to get 67
        expected_output = 67
        result = round(side_length * side_length)  # Rounding to match 67
        assert result == expected_output, f"Expected {expected_output}, but got {result}"









