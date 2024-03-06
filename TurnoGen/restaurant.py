class Restaurant:  
    def __init__(self, employees=None):
        """
        Constructor de la clase Restaurant.
        
        Args:
        - employees: Lista opcional de empleados del restaurante.
        """
        # Si no se proporciona ninguna lista de empleados, se inicializa como una lista vacía
        self.employees = employees or []

    def add_employee(self, employee):
        """
        Agrega un nuevo empleado a la lista de empleados del restaurante.

        Args:
        - employee: El empleado a agregar.
        """
        self.employees.append(employee)

    def remove_employee(self, employee):
        """
        Elimina un empleado de la lista de empleados del restaurante.

        Args:
        - employee: El empleado a eliminar.
        """
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"{employee} no se encontró en la lista de empleados.")

    def update_employee(self, old_employee, new_employee):
        """
        Actualiza la información de un empleado en la lista de empleados del restaurante.

        Args:
        - old_employee: El empleado cuya información se va a actualizar.
        - new_employee: El nuevo empleado con la información actualizada.
        """
        if old_employee in self.employees:
            index = self.employees.index(old_employee)
            self.employees[index] = new_employee
            print(f"Empleado actualizado: {old_employee} -> {new_employee}")
        else:
            print(f"{old_employee} no se encontró en la lista de empleados.")

# Ejemplo de uso
if __name__ == "__main__":
    restaurant = Restaurant()
    print("Lista de empleados inicial:", restaurant.employees)

    # Agregar empleados
    restaurant.add_employee("Juan")
    restaurant.add_employee("María")
    print("Lista de empleados después de agregar:", restaurant.employees)

    # Eliminar un empleado
    restaurant.remove_employee("Juan")
    print("Lista de empleados después de eliminar:", restaurant.employees)

    # Actualizar un empleado
    restaurant.update_employee("María", "Pedro")
    print("Lista de empleados después de actualizar:", restaurant.employees)
