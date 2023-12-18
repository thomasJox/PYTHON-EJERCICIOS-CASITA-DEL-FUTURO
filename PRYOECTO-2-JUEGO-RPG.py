import random

class Arma:
    def __init__(self,nombre,danio):
        self.nombre = nombre
        self.danio = danio

class Personaje:
    def __init__(self, nombre, vida, ataque_base, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque_base = ataque_base
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.arma = None

    def atacar(self, enemigo):
        raise NotImplementedError("Método de ataque no implementado")

    def recibir_danio(self, danio):
        danio_recibido = max(0, danio - self.defensa)
        self.vida -= danio_recibido
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} recibe {danio_recibido} de daño. Vida restante: {self.vida}")
        
    def equipar_arma(self, arma):
        self.arma = arma

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque_base=15, defensa=10, inteligencia=5, agilidad=5, fuerza=20)
        self.armas = [Arma("Espada", 10), Arma("Hacha", 12)]

    def atacar(self, enemigo):
        if self.arma:
            danio = self.ataque_base + self.fuerza + self.arma.danio
        else:
            danio = self.ataque_base + self.fuerza
        enemigo.recibir_danio(danio)

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque_base=20, defensa=5, inteligencia=25, agilidad=10, fuerza=5)
        self.armas = [Arma("Vara Magica", 8), Arma("Libro de Hechizos", 10)]

    def atacar(self, enemigo):
        if self.arma:
            danio = self.ataque_base + self.inteligencia + self.arma.danio
        else:
            danio = self.ataque_base + self.inteligencia
        enemigo.recibir_danio(danio)

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque_base=18, defensa=8, inteligencia=10, agilidad=20, fuerza=10)
        self.armas = [Arma("Arco", 9), Arma("Dagas", 11)]
        
    def atacar(self, enemigo):
        if self.arma:
            danio = self.ataque_base + self.agilidad + self.arma.danio
        else:
            danio = self.ataque_base + self.agilidad
        enemigo.recibir_danio(danio)

class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=75, ataque_base=22, defensa=5, inteligencia=15, agilidad=25, fuerza=15)
        self.armas = [Arma("Dagas Envenenadas", 12), Arma("Hoja Oculta", 14)]
         
    def atacar(self, enemigo):
        if self.arma:
            danio = (self.ataque_base + self.agilidad + self.inteligencia) * 1.5 + self.arma.danio
        else:
            danio = (self.ataque_base + self.agilidad + self.inteligencia) * 1.5
        enemigo.recibir_danio(danio)

class Enemigo(Personaje):
    def __init__(self, nombre, vuelo=False):
        super().__init__(nombre, vida=80, ataque_base=15, defensa=8, inteligencia=10, agilidad=15, fuerza=15)
        self.vuelo = vuelo

    def atacar(self, personaje):
        danio = self.ataque_base
        personaje.recibir_danio(danio)

# Función para determinar el orden de ataque basado en agilidad
def determinar_orden(personajes):
    return sorted(personajes, key=lambda x: x.agilidad, reverse=True)

# Función para simular un encuentro
def simular_encuentro(jugador, enemigo):
    print(f"\nEncuentro: {jugador.nombre} vs {enemigo.nombre}")
    orden = determinar_orden([jugador, enemigo])

    for personaje in orden:
        if isinstance(personaje, Enemigo) and personaje.vuelo:
            evasion = random.choice([True, False])  # 50% de posibilidad de esquivar el ataque
            if evasion:
                print(f"{personaje.nombre} esquiva el ataque y no recibe daño.")
            else:
                personaje.atacar(jugador)
        else:
            personaje.atacar(jugador)

# Crear personaje jugador
nombre_jugador = input("Ingresa el nombre de tu personaje: ")
clase_jugador = input("Selecciona tu clase (Guerrero, Mago, Arquero, Asesino): ")
jugador = globals()[clase_jugador](nombre_jugador)

# Crear enemigos
enemigo_guerrero = Enemigo("Orco Guerrero")
enemigo_mago = Enemigo("Esqueleto Mago")
enemigo_arquero = Enemigo("Duende Arquero")
enemigo_asesino = Enemigo("Sombra Asesina", vuelo=True)

# Simular encuentros
simular_encuentro(jugador, enemigo_guerrero)
simular_encuentro(jugador, enemigo_mago)
simular_encuentro(jugador, enemigo_arquero)
simular_encuentro(jugador, enemigo_asesino)
