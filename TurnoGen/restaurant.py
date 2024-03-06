class Restaurant:
    def __init__(self, employees=None):
        self.employees = employees or []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
 
