class Employee:
    """
    Clase que representa a un empleado.

    Atributos:
        contract_type: El tipo de contrato del empleado.
        labor_responsibility: La responsabilidad laboral del empleado.
        shift_management_ability: La habilidad de gestión de turnos del empleado.
        email: El correo electrónico del empleado.
    """

    def __init__(self, contract_type, labor_responsibility, shift_management_ability, email):
        """
        Constructor de la clase Employee.

        Args:
            contract_type: El tipo de contrato del empleado.
            labor_responsibility: La responsabilidad laboral del empleado.
            shift_management_ability: La habilidad de gestión de turnos del empleado.
            email: El correo electrónico del empleado.
        """
        self.contract_type = contract_type
        self.labor_responsibility = labor_responsibility
        self.shift_management_ability = shift_management_ability
        self.email = email
        
    def create_default_employees(self):
        employees = [
            Employee("full-time", "waiter", True, "d'artgnan@example.com"),
            Employee("part-time", "waiter", False, "aramis@example.com"),
            Employee("full-time", "waiter", True, "athos@example.com"),
            Employee("part-time", "waiter", False, "portos@example.com"),
            Employee("full-time", "waiter", True, "alexanderdumas@example.com")
        ]
        return employees

