from datetime import datetime, time, timedelta

class BusinessHours:
    def __init__(self, opening_time, closing_time, exceptions=None):
        # Inicializa los horarios de apertura y cierre del negocio
        self.opening_time = opening_time
        self.closing_time = closing_time
        # Establece las excepciones para días específicos, si las hay
        self.exceptions = exceptions or {}

    def is_open(self, date):
        # Comprueba si el negocio está abierto en la fecha y hora dadas
        if date.weekday() in self.exceptions:
            # Si hay una excepción para este día de la semana, comprueba si la hora actual está dentro del rango de excepción
            exception_opening, exception_closing = self.exceptions[date.weekday()]
            return exception_opening <= date.time() <= exception_closing
        # Si no hay excepciones para este día, simplemente comprueba si la hora actual está dentro del horario de apertura normal
        return self.opening_time <= date.time() <= self.closing_time

class HorarioDeApertura:
    def __init__(self):
        # Inicializa una instancia de BusinessHours para representar los horarios de un negocio específico
        # En este caso, supongamos que estos son los horarios de trabajo estándar
        self.business_hours = BusinessHours(time(9, 0), time(18, 0))

    def is_open(self, date):
        # Delega la comprobación del estado de apertura al objeto BusinessHours asociado
        return self.business_hours.is_open(date)

# Ejemplo de uso
if __name__ == "__main__":
    horario = HorarioDeApertura()
    ahora = datetime.now()
    print("¿El negocio está abierto?" if horario.is_open(ahora) else "El negocio está cerrado")
