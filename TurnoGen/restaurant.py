from business_hours import BusinessHours

class Restaurant:
    def __init__(self, name, business_hours):
        self.name = name
        self.business_hours = business_hours
        self.employees = []
        self.shifts = []

    def add_employee(self, employee):
       
        self.employees.append(employee)

    def assign_shift(self, employee_id, shift):
       
        pass

    def set_business_hours(self, opening_time, closing_time):
        self.business_hours = BusinessHours(opening_time, closing_time)
