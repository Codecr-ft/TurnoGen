from Month import Month

class AnnualCalendar:
    def __init__(self, year):
        """
        Constructor de la clase AnnualCalendar.

        Args:
        - year: El año del calendario.
        """
        self.year = year
        self.months = [Month(name="Month " + str(i), num_days=30) for i in range(1, 13)]
