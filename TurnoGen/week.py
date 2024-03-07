from datetime import date, timedelta

class Week:
    """
    Clase que representa una semana.

    Atributos:
        start_date: La fecha de inicio de la semana.
        end_date: La fecha de fin de la semana.
    """

    def __init__(self, start_date, end_date):
        """
        Constructor de la clase Week.

        Args:
            start_date: La fecha de inicio de la semana.
            end_date: La fecha de fin de la semana.
        """
        self.start_date = start_date
        self.end_date = end_date

class WeeklyCalendar:
    """
    Clase que representa un calendario semanal para un año específico.

    Atributos:
        year: El año del calendario.
        weeks: La lista de semanas en el calendario.
    """

    def __init__(self, year):
        """
        Constructor de la clase WeeklyCalendar.

        Args:
            year: El año del calendario.
        """
        self.year = year
        self.weeks = []

        # Definir el calendario semanal
        start_date = date(year, 1, 1)  # Comenzar desde el primer día del año
        while start_date.year == year:  # Continuar hasta el final del año
            end_date = start_date + timedelta(days=6)  # La semana termina después de 6 días
            self.weeks.append(Week(start_date, end_date))  # Agregar la semana a la lista
            start_date += timedelta(days=7)  # Moverse al inicio de la siguiente semana
