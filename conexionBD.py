##Conexion a la base de datos

from distutils.log import info
import email
from logging import exception
from multiprocessing import connection
from re import I
from select import select
from tkinter import N
from traceback import print_tb
import pyodbc 
from datetime import datetime

'''Variables SQL'''
server = 'DKTP-KBARRANTES'
bd = 'resHotelBD'
usuario = 'KevinBarrantes'
contraseña = 'Kjhy2002#'

'''String de conexion'''
try:
    conexion = pyodbc.connect('DRIVER={SQL Server}; \
                              SERVER='+server+'; \
                              DATABASE='+bd+';\
                              UID='+usuario+'; \
                              PWD='+contraseña)
    print('conexion buena')
except Exception as ex:
    print('Error: ', ex)

'''Metodos SQL'''

def sqlCons(sel):
    try:
        with conexion.cursor() as cursor:
            cursor.execute(sel)
            rows = cursor.fetchall()
            return rows
    except BaseException as ex:
        print('Error: ', ex)
    finally:
        cursor.close()

def infoCliente(ID):
    infoCliente = sqlCons(f'Select * from Cliente where ID_CLIENTE = {ID}')
    for row in infoCliente:
        print(row)
    

    
def sqlInsertCliente(ID,NOM,APELL,TEL,EMAIL):
    try:
        cursorIns = conexion.cursor()
        sql = f'''Insert Into Cliente (ID_CLIENTE, NOM_CLIENTE, APELL_CLIENTE, TEL_CLIENTE, EMAIL_CLIENTE)
                Values('{ID}','{NOM}','{APELL}','{TEL}','{EMAIL}')'''
        
        cursorIns.execute(sql)
        #n = cursorIns.rowcount
        cursorIns.commit()
        #return n
    except BaseException as ex:
        print('Error: ', ex)
    finally:
        cursorIns.close()

def sqlReservacion(ID,HAB,CHECKIN,CHECKOUT):
    try:
        cursorIns = conexion.cursor()
        sql = f'''Insert Into Reservacion (ID_RESERVADO, HAB_RESERVADA,DAT_CHECK_IN, DAT_CHECK_OUT)
                Values('{ID}','{HAB}','{CHECKIN}','{CHECKOUT}')'''
        
        cursorIns.execute(sql)
        #n = cursorIns.rowcount
        cursorIns.commit()
        #return n
    except BaseException as ex:
        print('Error: ', ex)
    finally:
        cursorIns.close()

def delCliente(delete):
    try:
        cursorDel = conexion.cursor()
        cursorDel.execute(delete)
        #n = cursorIns.rowcount
        cursorDel.commit()
        #return n
    except BaseException as ex:
        print('Error: ', ex)
    finally:
        cursorDel.close()


        


#print(sqlCons('select * from Cliente'))
# print('---------------------------------------')
insert = sqlInsertCliente('305390775', 'Kevin', 'Barrantes', '89676086', 'kev@gmail.com')
#delete = delCliente('DELETE FROM Cliente')
# print(sqlCons('select * from Cliente'))
# print(infoCliente(3232))


# sqlReservacion('13131','2','2022-12-12','2022-10-08')
# print(sqlCons('select * from Reservacion'))

