class Perro:
    def __init__(self, comida, juego, descanso):
        self.comida = comida
        self.juego = juego
        self.descanso = descanso 

    def feliz(self):
        return f"{self.comida} hace feliz al perro: ¡Guau, guau!"
    
def ingresar_datos():
    # Ingresar datos para el Perro
    print("¿como hizo feliz a su perro?...")
    comida_perro = input("alimento de hoy: ")
    juego_perro = input("cual fue el juego de hoy:")
    descanso_perro = int(input ("cuantas horas descanso el perro: "))

    perro=perro(comida_perro, juego_perro, descanso_perro)
    return perro 
def main():
    perro=ingresar_datos()
    print("felicidad del perro:")
    print(f" el perro comio {perro.comida}, jugaron con el al {perro.juego} y durmior {perro.descanso} horas. Por lo tanto el perro esta feliz ")
    if __name__ == "__main__":
        main()


