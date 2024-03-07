from employee import Employee  # Importar la clase Employee desde el archivo employee.py

class Restaurant:
    def __init__(self):
        """
        Constructor de la clase Restaurant.
        """
        self.employees = []

    def add_employee(self, employee):
        """
        Agrega un nuevo empleado al restaurante.
        
        Args:
        - employee: Objeto Employee a agregar.
        """
        self.employees.append(employee)

    def remove_employee(self, employee):
        """
        Elimina un empleado del restaurante.
        
        Args:
        - employee: El objeto Employee a eliminar.
        """
        self.employees = [e for e in self.employees if not e == employee]

    def update_employee(self, old_employee, new_employee):
        """
        Actualiza la información de un empleado en la lista de empleados del restaurante.
        
        Args:
        - old_employee: El objeto Employee cuya información se va a actualizar.
        - new_employee: El nuevo objeto Employee con la información actualizada.
        """
        for i, e in enumerate(self.employees):
            if e == old_employee:
                self.employees[i] = new_employee
                print(f"Empleado actualizado: {old_employee} -> {new_employee}")
                return
        print(f"{old_employee} no se encontró en la lista de empleados.")
