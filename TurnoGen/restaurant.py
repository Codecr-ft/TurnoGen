class Restaurant:
    def __init__(self, employees=[]):
        self.employees = employees

# Ejemplo de uso
if __name__ == "__main__":
    restaurant = Restaurant()
    print("Lista de empleados inicial:", restaurant.employees)

    # Agregar empleados
    restaurant.employees.append("Juan")
    restaurant.employees.append("María")
    print("Lista de empleados después de agregar:", restaurant.employees)

    # Eliminar un empleado
    if "Juan" in restaurant.employees:
        restaurant.employees.remove("Juan")
    print("Lista de empleados después de eliminar:", restaurant.employees)

    # Actualizar un empleado
    for i in range(len(restaurant.employees)):
        if restaurant.employees[i] == "María":
            restaurant.employees[i] = "Pedro"
            print("Empleado actualizado: María -> Pedro")
            break
    print("Lista de empleados después de actualizar:", restaurant.employees)
