import unittest
from lab7.task1.src.task1 import min_coins
from utils import measure

class TestMinCoins(unittest.TestCase):
    def test_should_handle_basic_case(self):
        
        # given
        money = 6
        coins = [1, 3, 4]
        expected_result = 2  # 3 + 3
        expected_time = 1

        # then
        result = min_coins(money, coins)
        time, _ = measure(min_coins, money, coins)

        # when
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time, expected_time)

    def test_should_handle_impossible_case(self):

        # given
        money = 7
        coins = [2, 4]
        expected_result = -1  # Размен невозможен

        # then
        result = min_coins(money, coins)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_large_input(self):

        # given
        money = 1000
        coins = [1, 5, 10, 25]
        expected_result = 40  # 40 монет номинала 25

        # then
        result = min_coins(money, coins)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_single_coin_type(self):

        # given
        money = 9
        coins = [3]
        expected_result = 3  # 3 + 3 + 3

        # then
        result = min_coins(money, coins)

        # when
        self.assertEqual(result, expected_result)

    def test_should_handle_zero_money(self):
        
        # given
        money = 0
        coins = [1, 2, 5]
        expected_result = 0  # Для суммы 0 нужно 0 монет

        # then
        result = min_coins(money, coins)

        # when
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
