from datetime import time

class Shift:
    """
    Clase que representa un turno de trabajo.

    Atributos:
        check_in: La hora de inicio del turno.
        type_workday: El tipo de jornada laboral ('completa' o 'partida').
        check_out: La hora de finalización del turno, calculada automáticamente.
    """

    def __init__(self, check_in, type_workday):
        """
        Constructor de la clase Shift.

        Args:
            check_in: La hora de inicio del turno.
            type_workday: El tipo de jornada laboral ('completa' o 'partida').
        """
        self.check_in = check_in
        self.type_workday = type_workday
        self.check_out = self.get_check_out()

    def get_check_out(self):
        """
        Método para calcular la hora de finalización del turno.

        Returns:
            La hora de finalización del turno.
        """
        if self.type_workday == 'completa':
            new_hour = (self.check_in.hour + 8)
        elif self.type_workday == 'partida':
            new_hour = (self.check_in.hour + 4)
        else:
            raise ValueError(f"Tipo de jornada {self.type_workday} no válido, escriba 'completa' o 'partida'.")
        return time(new_hour, self.check_in.minute)

