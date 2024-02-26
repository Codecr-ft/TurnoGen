from datetime import datetime, time

class BusinessHours:
    def __init__(self, opening_time, closing_time):
        # Inicializa los horarios de apertura y cierre del negocio
        self.opening_time = opening_time
        self.closing_time = closing_time

    def is_open(self, date):
        # Comprueba si el negocio está abierto en la fecha y hora dadas
        return self.opening_time <= date.time() <= self.closing_time

# Ejemplo de uso
if __name__ == "__main__":
    business_hours = BusinessHours(time(9, 0), time(18, 0))
    ahora = datetime.now()
    print("¿El negocio está abierto?" if business_hours.is_open(ahora) else "El negocio está cerrado")
