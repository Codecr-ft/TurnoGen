class AnnualCalendar:
    def __init__(self, year):
        """
        Constructor de la clase AnnualCalendar.
        Args:
        - year: El año del calendario.
        """
        self.year = year
        self.weeks = {week_num: [] for week_num in range(1, 53)}  # Словарь для хранения дней недели

    def display(self):
        """
        Mostrar el calendario anual.
        """
        print(f"Calendario para el año {self.year}:")
        for week_num, days in self.weeks.items():
            print(f"Week {week_num}: {days}")