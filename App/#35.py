from datetime import datetime, timedelta

def get_workday(check_in, full_time=True):
    try:
        check_in = datetime.strptime(check_in, "%H:%M")
    except ValueError:
        print("Formato de hora incorrecto. Utiliza el formato HH:MM (por ejemplo, 09:00)")
        return

    check_out = check_in + timedelta(hours=8 if full_time else 4)
    
    return check_in.strftime("%H:%M"), check_out.strftime("%H:%M")

def main():
    check_in = input("Introduce la hora de entrada (formato HH:MM): ")
    type_journey = input("¿Es un turno de jornada completa? (s/n): ").lower()
    
    if type_journey == 's':
        full_time = True
    elif type_journey == 'n':
        full_time = False
    else:
        print("Opción inválida. Por favor, responde 's' para sí o 'n' para no.")
        return

    check_in, check_out = get_workday(check_in, full_time)
    
    if check_in and check_out:
        print("Rango de turno:")
        print(f"Hora de entrada: {check_in}")
        print(f"Hora de salida: {check_out}")

if __name__ == "__main__":
    main()

