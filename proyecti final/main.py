import os
import re
import json
from uuid import uuid4

# Leer DB
def read_db():

    db = open( './bd.json', "r" ) 
    data = json.load( db ) 

    db.close()
    return data

# Guardar en DB
def save_db( person, method, account = "" ):

    data = read_db()
    with open( './bd.json', "w" ) as db:
        match method:
            case 'save':
                data.append( person )
                json.dump( data, db )                
                db.close()
            case 'update':
                list_to_update = list( filter(lambda x: x['account'] != account, data) )
                list_to_update.append( person )
                json.dump( list_to_update, db )                
                db.close()

# Clase persona
class Person():

    is_name = False

    def __init__(self, name, lastName) -> None:

        self.name = name
        self.lastname = lastName
        self.complete_name = f'{self.name} {self.lastname}'

        self.verify_user_name()
    
    def verify_user_name( self ):

        # Example name = John Smith
        self.is_name = bool( 
            re.fullmatch( 
                '[A-Za-z]{2,25}( [A-Za-z]{2,25})?', 
                self.complete_name  
            ) 
        )

# Clase Cliente
class Client():

    account = None
    bnk_balance = 0

    def __init__(self, person ) -> None:
        self.person = person
    
    def create_account( self ):
        
        if self.person.is_name:
        
            data = read_db()

            for person in data:
                if self.person.name == person["name"] and self.person.lastname == person["lastname"]:
                    print( 'El usuario ya existe' )
                    input( '\nEnter para continuar' )
                    return False

            new_account = str(uuid4()).split('-')
            self.account = new_account[-1] + new_account[-2]

            new_person = {
                "name": self.person.name, 
                "lastname": self.person.lastname,
                "account": self.account,
                "bnk_balance": self.bnk_balance 
            }

            save_db( new_person, 'save' )
            print( f'Tu numero de cuenta es: { self.account }' )

            input( '\nEnter para continuar' )
            return True 

        else:
            print('Los datos ingresados son incorrectos')

            input( '\nEnter para continuar' )
            return False  

    def account_details():
        pass

# Clase banco - logica del banco
class Bank():  

    user = ""

    def __init__( self, account_num = "" ) -> None:
        self.account = account_num


    # Buscar usaurio
    def search_user(self, account):
        data = read_db()
        res = list( filter(lambda x: x['account'] == account, data) )

        if len( res ) != 0:
            return res
        
        print( 'No se ha encontrado al usuario' )
        input( '\nEnter para continuar' )
        return False
    
    # Crear cuenta
    def create_account( self, name, lastname ):

        new_person = Person( name, lastname )
        new_client = Client( new_person )

        new_client.create_account()
        
    # Checar balance
    def check_balance( self ):

        # Busca al usuario
        self.user = self.search_user( self.account )[0]

        print( 'Cuenta en pesos:')
        print( f'${self.user["bnk_balance"]} MXN' )
        
        input( '\nEnter para continuar' )
        pass

    # Depositar a cuenta
    def deposit_own_account(self, amount):
        
        # Busca al usuario
        self.user = self.search_user( self.account )[0]

        if amount > 0: 
            self.user["bnk_balance"] += amount
            
            # Salvar en la base de datos
            save_db( self.user, 'update', self.account )

            print( f"Has depositado { amount } pesos a tu cuenta" )
            input( '\nEnter para continuar' )
        else:
            print('Cantidad incorrecta o no valida')
            input( '\nEnter para continuar' )
        
    
    # Deposito a terceros
    def deposit_to_third_parties(self, third_party_account, amount):
        
        target_user =  self.search_user( third_party_account )[0]
        
        if amount > 0: 
            target_user["bnk_balance"] += amount 

            #update in database
            save_db( target_user, 'update', third_party_account )

            print( f"Has depositado { amount } pesos a cuenta de terceros" )
            input( '\nEnter para continuar' )
        else:
            print('Cantidad incorrecta o no valida')
            input( '\nEnter para continuar' )

    # Retirar
    def withdrawals( self, amount ):
        self.user = self.search_user( self.account )[0]

        if amount > 0 and amount < self.user["bnk_balance"]:
            
            self.user["bnk_balance"] -= amount

            save_db( self.user, 'update', self.account )

            print( f'Has retirado {amount}.' )
            print( f'Tu saldo total es de: { self.user["bnk_balance"] }' )
            input( '\nEnter para continuar' )
        else: 
            print('Cantidad incorrecta o no valida')
            input( '\nEnter para continuar' )


def app():

    AUTH_OPTIONS = [
        "[0] - Crea una cuenta",
        "[1] - Ingresar",
        "[q] - Salir"
    ]

    BANK_OPTIONS = [
        "[0] - Checa tu saldo",
        "[1] - Deposita a tu cuenta",
        "[2] - Deposita a terceros",
        "[3] - Retiro",
        "[q] - Salir",
    ]

    while True:

        os.system( 'clear' or 'cls' )
        print( '----------------------' )
        print( '  Bienvenido a BBDVA  ' )
        print( '----------------------' )

        for auth_opt in AUTH_OPTIONS:
            print( auth_opt )
        
        print("\n")
        user_input = input("Escoge una opción: ")

        match user_input:
            case '0':
                os.system( 'clear' or 'cls' )
                print( '--------------' )
                print( '  Formulario  ' )
                print( '--------------' )
                
                name = str( input('Cuál es tu nombre?: '))
                apellido = str( input('Cuál es tu apellido?: '))

                os.system( 'clear' or 'cls' )
                Bank().create_account( name, apellido )
            case '1':

                while True:
                    account = str( input('Ingresa el numero de tu cuenta: ' ))
                    user_account = Bank().search_user( account )
                    
                    if not user_account:
                        break 

                    user_account = Bank( account )
                
                    while True:
                        os.system( 'clear' or 'cls' )
                        print( '-------------------------' )
                        print( '  Bienvenido a tu banco  ' )
                        print( '-------------------------' )
                        for bank_option in BANK_OPTIONS:
                            print( bank_option )
                        print("\n")
                        bank_option_choice = input("Escoge una opción: ")   

                        match bank_option_choice:
                            case '0':
                                os.system( 'clear' or 'cls' )
                                user_account.check_balance()
                            case '1':
                                os.system( 'clear' or 'cls' )
                                amount = float( input( 'Cuanto dinero quieres ingresar: ' ))
                                user_account.deposit_own_account( amount )

                            case '2':
                                os.system( 'clear' or 'cls' )
                                third_account = str( input( 'Numero de cuenta del beneficiario: ' ))
                                amount = float( input( 'Cuanto dinero quieres depositar: ' ))
                                user_account.deposit_to_third_parties( third_account, amount )
                            case '3':
                                os.system( 'clear' or 'cls' )
                                amount = float( input( 'Cuanto dinero quieres retirar: ' ))
                                user_account.withdrawals( amount )
                            case 'q':
                                break
                            case other:
                                print( f'{ other } no es valido' )
                                input( '\nEnter para continuar' )
                    break

            case 'q':
                os.system( 'clear' or 'cls' )
                print( 'Gracias por preferirnos' )
                break
                
            case other:
                print( f'{ other } no es valido' )
                input( '\nEnter para continuar' )



    pass

    
def main():
    app()
    

main()