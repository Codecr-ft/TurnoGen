# #35 Generar horario de un día

class Dia:
    def __init__(self):
        self.horario_apertura = []

    def dividir_en_medias_horas(self):
        for hora in range(11, 24):
            self.horario_apertura.append(f"{hora}:00 / {hora}:30")
            self.horario_apertura.append(f"{hora}:30 / {hora+1}:00")

    def obtener_horario_apertura(self):
        return self.horario_apertura

def main():
    mi_dia = Dia()
    mi_dia.dividir_en_medias_horas()
    lista_horario_apertura = mi_dia.obtener_horario_apertura()
    
    print("\nHorario de apertura:")
    for hora_apertura in lista_horario_apertura:
        print(hora_apertura)

if __name__ == "__main__":
    main()