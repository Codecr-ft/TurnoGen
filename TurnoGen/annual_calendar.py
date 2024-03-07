from month import Month

class AnnualCalendar:
    def __init__(self, year):
        """
        Constructor de la clase AnnualCalendar.
        Args:
        - year: El año del calendario.
        """
        self.year = year
        self.months = [Month(name="Month " + str(i), num_days=self.get_num_days(i)) for i in range(1, 13)]

    def get_num_days(self, month):
        """
        Devuelve el número de días en un mes.
        Args:
        - month: El número del mes.
        """
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 28  # Febrero tiene 28 días por defecto, no consideramos los años bisiestos

