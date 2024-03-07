class Employee:
    def __init__(self, contract_type, labor_responsibility, shift_management_ability, email):
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
