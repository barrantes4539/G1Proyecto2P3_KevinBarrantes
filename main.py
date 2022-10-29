from os import system
from select import select
from shutil import register_archive_format
from traceback import print_tb
from datetime import datetime


import conexionBD as bd
class main:
    def portal():
        print('---Bienvenido al sistema de reservación del hotel---'
              '\n1. Registrar cliente'
              '\n2. Clientes registrados'
              '\n3. Clientes activos'
              '\n4. Check in'
              '\n5. Check out'
              '\n6. Salir')
    def registrar():
        idCliente = str(input('Identificacion: '))
        nomCliente = str(input('Nombre: '))
        apellCliente = str(input('Apellido: '))
        telCliente = str(input('Telefono: '))
        emailCliente = str(input('Email: '))
        registrar = input('¿Desea registrar este cliente? s/n\n')
        if registrar == 's':
            bd.sqlInsertCliente(idCliente, nomCliente, apellCliente, telCliente, emailCliente)

    def checkIn():

        infoCliente = bd.sqlCons('select * from Cliente')
        infoHabitacion = bd.sqlCons('select * from Habitacion')

        print('----Check in----')
        print('\n**Habitaciones disponibles y costos**\n')
        for row in infoHabitacion:
           print(f'{row[0]},{str(row[1])},{row[2]}\n')

        

        chIDCliente = str(input('Introduzca el numero de identificacion del cliente: '))
        chHab = int(input('Digite el numero de habitacion que desea reservar: '))
        chDateIn = str(datetime.today().strftime('%Y-%m-%d'))
        chDateOut = str(input('Introduzca el dia de checkout del cliente FORMATO(%Y-%m-%d): '))

        bd.sqlReservacion(chIDCliente, chHab, chDateIn, chDateOut)
                        

                
               



        
        
        
    


# for row in bd.sqlCons('Select * from Cliente'):
#            print(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}')

# p = main.portal()
# r = main.registrar()
ch = main.checkIn()
