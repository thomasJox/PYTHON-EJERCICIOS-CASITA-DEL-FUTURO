# PROYECTO FINAL PYTHON
# CAJERO AUTOMATICO CON FUNCIONRD EXTRAS
clave="python"
clave_ingresada=""
saldo_inicial=15000
desicion="si"
operacion=0
cantidad_operada=0
nuevo_saldo=0

print("CAJERO AUTOMATICO")
clave_ingresada=input("ingrese su clave porfavor: ")
if(clave_ingresada==clave):
    print("*************Bievenido*************")
    print("")
    while(desicion=="si"):
        print("Que desea hacer?")
        print("1. Consultar saldo")
        print("2. Retiro")
        print("3. Deposito")
        operacion=int(input("ingrese la operacion a realizar "))
        # operacion de consulta de saldos
        if(operacion==1):
            print("usted a consultado su saldo y es de: $"+str(saldo_inicial)+ "Pesos")
            print("")
        # operacion de retiros
        elif(operacion==2):
            print("usted a seleccionado retirar dinero de su cuenta")
            cantidad_operada=int(input("cuanto desea retirar? "))
            if(cantidad_operada<saldo_inicial):
                nuevo_salvo=saldo_inicial-cantidad_operada
                saldo_inicial=nuevo_saldo
                print("Retiro exitoso")
            else:
                print("fondos insuficientes")
        elif(operacion==3):
            print("usted a seleccionado la opcion de deposito")
            cantidad_operada=int(input("cuanto desea depositar"))
            nuevo_saldo=saldo_inicial+cantidad_operada
            saldo_inicial=nuevo_saldo
            print("deposito exitoso")
            print("")
        
        
        desicion=input("Desea realizar otra operacion? si/no " )
        


else:
    print("Contraseña incorrecta")