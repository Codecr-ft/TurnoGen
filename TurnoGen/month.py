from day import Day

class Month:
    def __init__(self, name, month, year):
        """
        Constructor de la clase Month.

        Args:
        - name: El nombre del mes.
        - month: El número del mes (1 para enero, 2 para febrero, etc.).
        - year: El año.
        """
        self.name = name
        self.month = month
        self.year = year
        

        if month in (1, 3, 5, 7, 8, 10, 12):
            self.num_days = 31
        elif month in (4, 6, 9, 11):
            self.num_days = 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                self.num_days = 29
            else:
                self.num_days = 28
        else:
            self.num_days = 0  
        self.days = [Day(date=i) for i in range(1, self.num_days + 1)]