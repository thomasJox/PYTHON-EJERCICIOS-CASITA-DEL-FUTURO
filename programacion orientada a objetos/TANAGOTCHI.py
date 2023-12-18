# NOTA IMPORTANTE EL ARCHIVO JSON QUE CONTIENE EL ESTADO DEL TAMAGOTCHI SE GUARDA EN EL SITIO USUARIOS DEL PC DENTRO DEL USURIO QUE LO ESTE EJECUTANDO, EJEMPLO: C:\Users\JOAKO301

import json

class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = "mocco"
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"{self.nombre}:")
        print(f"Nivel de Energía: {self.nivel_energia}")
        print(f"Nivel de Hambre: {self.nivel_hambre}")
        print(f"Estado de Humor: {self.humor}")
        print("----------------------")

    def alimentar(self):
        self.nivel_hambre -= 10
        self.nivel_energia -= 15
        self.verificar_estado()
        self.guardar_estado()

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10
        self.verificar_estado()
        self.guardar_estado()

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5
        self.verificar_estado()
        self.guardar_estado()

    def verificar_estado(self):
        if self.nivel_energia <= 0:
            self.esta_vivo = False
        elif self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            self.verificar_estado()

        if self.nivel_felicidad <= 0:
            self.humor = "enojado"
        elif self.nivel_felicidad <= 30:
            self.humor = "triste"
        elif self.nivel_felicidad <= 70:
            self.humor = "indiferente"
        elif self.nivel_felicidad <= 100:
            self.humor = "feliz"
        else:
            self.humor = "eufórico"

    def guardar_estado(self):
        estado = {
            "nombre": self.nombre,
            "nivel_energia": self.nivel_energia,
            "nivel_hambre": self.nivel_hambre,
            "nivel_felicidad": self.nivel_felicidad,
            "humor": self.humor,
            "esta_vivo": self.esta_vivo
        }
        with open(f"{self.nombre}_estado.json", "w") as file:
            json.dump(estado, file)

    def cargar_estado(self):
        try:
            with open(f"{self.nombre}_estado.json", "r") as file:
                estado = json.load(file)
                self.nombre = estado["nombre"]
                self.nivel_energia = estado["nivel_energia"]
                self.nivel_hambre = estado["nivel_hambre"]
                self.nivel_felicidad = estado["nivel_felicidad"]
                self.humor = estado["humor"]
                self.esta_vivo = estado["esta_vivo"]
        except FileNotFoundError:
            print("No se encontró un archivo de estado para cargar.")


# Ejemplo de uso:
mi_tamagotchi = Tamagotchi("mocco")

# Intento de cargar el estado anterior
mi_tamagotchi.cargar_estado()

mi_tamagotchi.mostrar_estado()

mi_tamagotchi.alimentar()
mi_tamagotchi.mostrar_estado()

mi_tamagotchi.jugar()
mi_tamagotchi.mostrar_estado()

mi_tamagotchi.dormir()
mi_tamagotchi.mostrar_estado()
