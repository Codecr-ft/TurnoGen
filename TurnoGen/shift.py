from datetime import time

class Shift:
    def __init__(self, check_in, type_workday):
        self.check_in = check_in
        self.type_workday = type_workday
        self.check_out = self.get_check_out()

    def get_check_out(self):
        if self.type_workday == 'completa':
            new_hour = (self.check_in.hour + 8)
        elif self.type_workday == 'partida':
            new_hour = (self.check_in.hour + 4)
        else:
            raise ValueError(f"Tipo de jornada {self.type_workday} no válido, escriba 'completa' o 'partida'.")
        return time(new_hour, self.check_in.minute)