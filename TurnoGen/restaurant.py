class Restaurant:
    """
    Representa un restaurante.

    Atributos:
        business_hours (str): The business hours of the restaurant.
        name (str): The name of the restaurant.
        employees (list): The list of employees working at the restaurant.
        shifts (dict): The shifts available at the restaurant, categorized as 'completo' and 'partido'.
    """

    def __init__(self, business_hours, name, employees):
        """
        Inicializa una instancia de la clase Restaurant.

        Parámetros:
            business_hours (str): Las horas de funcionamiento del restaurante.
            name (str): El nombre del restaurante.
            employees (list): La lista de empleados que trabajan en el restaurante.

        Atributos:
            name (str): El nombre del restaurante.
            business_hours (str): Las horas de funcionamiento del restaurante.
            employees (list): La lista de empleados que trabajan en el restaurante.
            shifts (dict): Los turnos disponibles en el restaurante, categorizados como 'completo' y 'partido'.
        """
        self.name = name
        self.business_hours = business_hours  
        self.employees = employees
        self.shifts = {'completo': [], 'partido': []}
