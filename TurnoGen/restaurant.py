class Restaurant:
    def __init__(self, business_hours, name, employees):
        self.name = name
        self.business_hours = business_hours  
        self.employees = employees
        self.shifts = {'completo': [], 'partido': []} 