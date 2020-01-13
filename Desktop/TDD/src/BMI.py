
class BMI:

    @staticmethod
    def bmi(height, weight):
        if (height <= 0):
            return("Invalid height value")
        elif (weight <= 0):
            return("Invalid weight value")
        else:
            return round(weight / (height * height), 2)

    @staticmethod
    def bmiMeasure(bmi):
        if (bmi <= 0): return "Invalid BMI value"
        if (0 < bmi < 18.5): return "Underweight"
        elif (18.5 <= bmi < 25): return "Normal"
        elif (25 <= bmi <= 29.9): return "Overweight"
        elif (30 <= bmi <= 34.9): return "Obese class I"
        elif (35 <= bmi <= 39.9): return "Obese class II"
        else: return "Obese class III"

