import pytest

from myapp.app import multiply_by_two, divide_by_two


@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a,b]


class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    def test_student_id_calculation(self):
    student_id_last_two_digits = 25  # Replace with your actual last two digits
    expected_output = 9999  # Incorrect expected output to force failure
    assert multiply_by_two(student_id_last_two_digits) == expected_output


