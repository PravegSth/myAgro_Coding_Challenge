import unittest
from calculate_days_of_power import get_days_of_power


class Test(unittest.TestCase):
    def test_daysOfPower(self):
        self.assertEqual(get_days_of_power(3000,3,500,10,1500,7,700000), 141)
        self.assertEqual(get_days_of_power(500,3,500,10,500,7,21000), 17)
        self.assertEqual(get_days_of_power(1300,0,500,0,1500,7,10000), 5)
        self.assertEqual(get_days_of_power(10000,3,500,10,1500,7,11000), 1)


if __name__ == '__main__':
    unittest.main()