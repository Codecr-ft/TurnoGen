from employee import Employee  # Importar la clase Employee desde el archivo employee.py

class Restaurant:
    def __init__(self):
        """
        Constructor de la clase Restaurant.
        """
        self.employees = []

    def add_employee(self, contract_type, labor_responsibility, shift_management_ability, email):
        """
        Agrega un nuevo empleado al restaurante.
        
        Args:
        - contract_type: Tipo de contrato del empleado.
        - labor_responsibility: Responsabilidad laboral del empleado.
        - shift_management_ability: Habilidad de gestionar turnos del empleado.
        - email: Correo electrónico del empleado.
        """
        employee = Employee(contract_type, labor_responsibility, shift_management_ability, email)
        self.employees.append(employee)

    def remove_employee(self, employee):
        """
        Elimina un empleado del restaurante.
        
        Args:
        - employee: El objeto Employee a eliminar.
        """
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"{employee} no se encontró en la lista de empleados.")

    def update_employee(self, old_employee, new_employee):
        """
        Actualiza la información de un empleado en la lista de empleados del restaurante.
        
        Args:
        - old_employee: El objeto Employee cuya información se va a actualizar.
        - new_employee: El nuevo objeto Employee con la información actualizada.
        """
        if old_employee in self.employees:
            index = self.employees.index(old_employee)
            self.employees[index] = new_employee
            print(f"Empleado actualizado: {old_employee} -> {new_employee}")
        else:
            print(f"{old_employee} no se encontró en la lista de empleados.")