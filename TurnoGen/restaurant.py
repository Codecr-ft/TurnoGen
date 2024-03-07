class Restaurant:
    def __init__(self, business_hours, name = "Carmelita"):
        self.name = name 
        self.business_hours = business_hours  
        self.employees = []  ## Por ahora sin empleados, estructura lista para añadir
        self.shifts = {'completo': [], 'partido': []}