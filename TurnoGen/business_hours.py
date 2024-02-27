from datetime import time

class BusinessHours:
    def __init__(self, opening_time_str: str, closing_time_str: str) -> None:
        self.opening_time: time = self.parse_time(opening_time_str)
        self.closing_time: time = self.parse_time(closing_time_str)

    def parse_time(self, time_str: str) -> time:
        hour, minute = map(int, time_str.split(':'))
        return time(hour, minute)

    

