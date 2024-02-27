from datetime import time

class Turno:
    def __init__(self, check_in, type_workday):
        self.check_in = check_in
        self.type_workday = type_workday
        self.check_out = self.get_check_out()

    def get_check_out(self):
        if self.type_workday == 'completa':
            check_out = self.add_hours(self.check_in, 8)
        elif self.type_workday == 'partida':
            check_out = self.add_hours(self.check_in, 4)
        else:
            raise ValueError("Tipo de jornada no válido")
        return check_out

    def add_hours(self, check_time, hours):
        new_hour = (check_time.hour + hours) % 24
        return time(new_hour, check_time.minute)

