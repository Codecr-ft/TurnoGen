from day import Day

class Month:
    """
    Clase que representa un mes en un calendario.

    Atributos:
        name: El nombre del mes.
        num_days: El número total de días en el mes.
        days: La lista de objetos Day que representan los días del mes.
    """

    def __init__(self, name, num_days):
        """
        Constructor de la clase Month.

        Args:
            name: El nombre del mes.
            num_days: El número total de días en el mes.
        """
        self.name = name
        self.num_days = num_days
        self.days = [Day(date=i) for i in range(1, num_days + 1)] 
