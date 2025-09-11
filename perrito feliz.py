class Perro:
    def __init__(self, comida, juego, descanso):
        self.comida = comida
        self.juego = juego
        self.descanso = descanso 

    def feliz(self):
        return f"{self.comida} hace feliz al perro: ¡Guau, guau!"
    
def ingresar_datos():
    # Ingresar datos para el Perro
    print("¿Cómo hizo feliz a su perro?")
    comida_perro = input("Alimento de hoy: ")
    juego_perro = input("¿Cuál fue el juego de hoy?: ")
    descanso_perro = int(input("¿Cuántas horas descansó el perro?: "))

    perro = Perro(comida_perro, juego_perro, descanso_perro)
    return perro 

def main():
    perro = ingresar_datos()
    print("Felicidad del perro:")
    print(f"El perro comió {perro.comida}, jugaron con el/la {perro.juego} y durmió {perro.descanso} horas. Por lo tanto, el perro está feliz.")

if __name__ == "__main__":
    main()
