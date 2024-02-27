class BusinessHours:
    def __init__(self, opening_time_str, closing_time_str):
        self.opening_time = self.parse_time(opening_time_str)
        self.closing_time = self.parse_time(closing_time_str)

    def parse_time(self, time_str):
        hour, minute = map(int, time_str.split(':'))
        return time(hour, minute)

    

