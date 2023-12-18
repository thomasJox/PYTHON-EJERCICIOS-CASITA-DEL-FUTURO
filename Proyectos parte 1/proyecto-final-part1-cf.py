#Cajero automatico

import time

print("---BIENVENIDO A TOMS ATM---")

#variables a usar
usuario = ""
pin = ""
saldo = 0
total_saldo = 0


#Funcion para crear la cuenta
def crear_cuenta():
    global usuario
    usuario = input("Ingrese su nombre completo: ")
    global pin
    pin = input("Ingrese su PIN: ")
    print("VALIDANDO...POR FAVOR ESPERE.")
    time.sleep(2)
    print(f"CUENTA CREADA CON EXITO {usuario}")
    pregunta =  input("¿Quiere ingresar saldo? (Si o no)")
    if pregunta == "si":
        ingresar_dinero()
        main()
    else:
        print("Gracias por confiar en TOMS ATM")

def retirar_dinero():
    global usuario, saldo_retirar
    global pin
    global saldo
    global total_saldo

    usuario_comprobar = input("Ingrese su usuario: ")
    pin_comprobrar = input("Ingrese su PIN: ")
    #Comprobar el usuario
    if usuario_comprobar == usuario and pin_comprobrar == pin:
        print(f"Su saldo es de: {total_saldo}")
        #Si no tiene dinero
        if total_saldo <= 0:
            print("No tiene saldo a retirar, ingrese dinero en su cuenta. ")
            ingresar_dinero()
            pregunta = input("¿Quiere retirar su dinero? (Si o No)")
            if pregunta == "si":
                retirar_dinero()
        #Si tiene mas saldo, retirar
        if total_saldo > 0:
            saldo_retirar = int(input("Por favor ingrese la cantidad a retirar: "))
            print("Retirando...Por favor espere.")
            time.sleep(2)
            print("RETIRADO CON EXITO")
            total_saldo = total_saldo - saldo_retirar
            print("Su saldo actual es: ", total_saldo)
    #Si los datos son incorrectos
    else:
        print("Sus datos son incorrectos!")
        retirar_dinero()

def ingresar_dinero():
    global usuario
    global pin
    global saldo
    global total_saldo
    usuario_comprobar = input("Ingrese su usuario: ")
    pin_comprobrar = input("Ingrese su PIN: ")
    # Comprobar el usuario
    if usuario_comprobar == usuario and pin_comprobrar == pin:
        saldo_nuevo = int(input("Ingrese la cantidad a ingresar a su cuenta: "))
        print("Ingresando...Por favor espere.")
        time.sleep(3)
        total_saldo = saldo + saldo_nuevo
        print("Ingresado con exito..\nSu saldo ahora es de: ", total_saldo)
        pregunta = input("¿Quiere retirar saldo? (Si o no)")
        if pregunta == "si":
            retirar_dinero()
        else:
            print("Gracias por su confianza")


def estado_cuenta():
    global usuario
    global pin
    global saldo
    global total_saldo
    usuario_comprobar = input("Ingrese su usuario: ")
    pin_comprobrar = input("Ingrese su PIN: ")
    if usuario_comprobar == usuario and pin_comprobrar == pin:
        print(f"Bienvenid@ {usuario}")
        print(f"Su saldo es de {total_saldo}")

def main():
    print("Por favor selecciona lo que quieres hacer: ")
    eleccion = input(("\n 1 para crear cuenta\n 2 para retirar dinero\n 3 para ingresar dinero\n 4 para revisar el estado de tu cuenta \n 5 para salir: "))

    if eleccion == "1":
        crear_cuenta()
    if eleccion == "2":
        retirar_dinero()
    if eleccion == "3":
        ingresar_dinero()
    if eleccion == "4":
        estado_cuenta()
    if eleccion == "5":
        print("Saliendo...por favor espere.")
        time.sleep(2)
        print("Sesion cerrada")

main()
