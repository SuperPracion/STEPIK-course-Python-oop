class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(value):
        return (value * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(value):
        return (value - 32) * 5/9

