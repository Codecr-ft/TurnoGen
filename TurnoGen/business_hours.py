from datetime import time

class BusinessHours:
    """
    Clase para representar las horas de apertura y cierre de un negocio.

    Attributes:
        opening_time (time): La hora de apertura del negocio.
        closing_time (time): La hora de cierre del negocio.
    """

    def __init__(self, opening_time_str: str, closing_time_str: str) -> None:
        """
        Constructor de la clase BusinessHours.

        Args:
            opening_time_str (str): Cadena de texto que representa la hora de apertura en formato HH:MM.
            closing_time_str (str): Cadena de texto que representa la hora de cierre en formato HH:MM.
        """
        self.opening_time: time = self.parse_time(opening_time_str)
        self.closing_time: time = self.parse_time(closing_time_str)

    def parse_time(self, time_str: str) -> time:
        """
        Método para analizar una cadena de texto y convertirla en un objeto de tiempo.

        Args:
            time_str (str): Cadena de texto que representa la hora en formato HH:MM.

        Returns:
            time: Objeto de tiempo creado a partir de la cadena de texto proporcionada.
        """
        hour, minute = map(int, time_str.split(':'))
        return time(hour, minute)


    

