class Calculator:

    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print("Calculation type: {0}". format(cls.calculation_type))
        return a * b
