import unittest
from src.BMI import BMI

class BMI_test(unittest.TestCase):
    def test_input_integrity_check1(self):
        # height
        h1 = 0.0
        h2 = -1.2
        h3 = 1.83

        # weight
        w1 = 0.0
        w2 = -1.3
        w3 = 80

        # assume
        expected1 = "Invalid height value"
        expected2 = "Invalid height value"
        expected3 = "Invalid weight value"
        expected4 = "Invalid weight value"
        expected5 = 23.89

        # action
        result1 = BMI.bmi(h1, 1)
        result2 = BMI.bmi(h2, 1)
        result3 = BMI.bmi(1, w1)
        result4 = BMI.bmi(1, w2)
        result5 = BMI.bmi(h3, w3)


        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)

    def test_input_integrity_check2(self):
        # bmi
        b1 = 0.0
        b2 = -1.2
        b3 = 23.89

        # assume
        expected1 = "Invalid BMI value"
        expected2 = "Invalid BMI value"
        expected3 = "Normal"

        # action
        result1 = BMI.bmiMeasure(b1)
        result2 = BMI.bmiMeasure(b2)
        result3 = BMI.bmiMeasure(b3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


if __name__ == '__main__':
    unittest.main()
