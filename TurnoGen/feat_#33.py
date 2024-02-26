from datetime import time

class BusinessHours:
    def __init__(self, opening_time, closing_time):
        self._opening_time = opening_time
        self._closing_time = closing_time

    @property
    def opening_time(self):
        return self._opening_time

    @property
    def closing_time(self):
        return self._closing_time

    def is_open_at(self, date_time):
        time_of_day = date_time.time()
        return self.opening_time <= time_of_day <= self.closing_time

