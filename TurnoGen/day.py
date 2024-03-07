class Day:
    """
    Clase que representa un día.

    Atributos:
        date: La fecha del día.
        working (bool): Un indicador booleano que especifica si el día es laborable. Por defecto es True.
        holiday (bool): Un indicador booleano que especifica si el día es festivo. Por defecto es False.
    """

    def __init__(self, date, working=True, holiday=False):
        """
        Constructor de la clase Day.

        Args:
            date: La fecha del día.
            working (bool): Un indicador booleano que especifica si el día es laborable. Por defecto es True.
            holiday (bool): Un indicador booleano que especifica si el día es festivo. Por defecto es False.
        """
        self.date = date
        self.working = working
        self.holiday = holiday

        