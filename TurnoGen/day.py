class Day:
    def __init__(self, date, working=True, holiday=False):
        """
        Constructor de la clase Day.

        Args:
        - date: La fecha del día.
        - working: Un booleano que indica si el día es laborable o no. Por defecto es True.
        - holiday: Un booleano que indica si el día es festivo o no. Por defecto es False.
        """
        self.date = date
        self.working = working
        self.holiday = holiday
        