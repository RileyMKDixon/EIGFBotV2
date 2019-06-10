import unittest
from lib.eigf_big_number.big_number import BigNumber

class BigNumberTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegexPattern(self):
        pattern1 = "1.23"
        pattern2 = "123.456"
        pattern3 = "0.12"
        pattern4 = "1.23k"
        pattern5 = "12.34uV"
        pattern6 = "123456.123456dS"
        pattern7F = ".5356"
        pattern8F = ".123k"
        pattern9F = "1.23abc"
        pattern10F = "-1.23"
        pattern11F = "12.34.56"
        pattern12 = "12Q"

        self.assertTrue(BigNumber.isValidBigNumber(pattern1))
        self.assertTrue(BigNumber.isValidBigNumber(pattern2))
        self.assertTrue(BigNumber.isValidBigNumber(pattern3))
        self.assertTrue(BigNumber.isValidBigNumber(pattern3))
        self.assertTrue(BigNumber.isValidBigNumber(pattern4))
        self.assertTrue(BigNumber.isValidBigNumber(pattern5))
        self.assertTrue(BigNumber.isValidBigNumber(pattern6))
        self.assertIsNone(BigNumber.isValidBigNumber(pattern7F))
        self.assertIsNone(BigNumber.isValidBigNumber(pattern8F))
        self.assertIsNone(BigNumber.isValidBigNumber(pattern9F))
        self.assertIsNone(BigNumber.isValidBigNumber(pattern10F))
        self.assertIsNone(BigNumber.isValidBigNumber(pattern11F))
        self.assertTrue(BigNumber.isValidBigNumber(pattern12))
        
    def doubleToBigNum(self):
        num1 = 123 * pow(10, 0)
        num2 = 234 * pow(10, 3)
        num3 = 345 * pow(10, 6)
        num4 = 456 * pow(10, 9)
        num5 = 567 * pow(10, 12)
        num6 = 678 * pow(10, 15)
        num7 = 789 * pow(10, 18)
        num8 = 890 * pow(10, 21)
        num9 = 901 * pow(10, 24)
        num10 = 1234 * pow(10, 27)
        num11 = 2345 * pow(10, 30)
        num12 = 3456 * pow(10, 33)
        num13 = 4567 * pow(10, 36)
        num14 = 5678 * pow(10, 39)
        num13 = 4567 * pow(10, 36)
        num14 = 5678 * pow(10, 39)
        num13 = 4567 * pow(10, 36)
        num14 = 5678 * pow(10, 39)
        

if __name__ == '__main__':
    unittest.main()

