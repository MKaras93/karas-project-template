from src.main import sum_numbers


class TestExample:
    def test_1_plus_1_equals_2(self):
        assert 1 + 1 == 2

    def test_sum_numbers(self):
        assert sum_numbers(1, 2) == 3
