import pandas as pd
from funciones import *
from ConPandas import *

# Llamando a la función de comandos
opcion = comandos()

if opcion == 1: # Create
    dictAutos = ingreso_datos()
    df = pd.DataFrame([dictAutos], columns=['MARCA', 'FABRICACION', 'COLOR', 'PRECIO', 'ESTADO'])
    try:
        first_read = pd.read_csv('registrados.csv')
        df.to_csv('registrados.csv', header=False, mode='a',index=False)
    except OSError as e:
        df.to_csv('registrados.csv', mode='a',index=False)
    print('\nAUTO REGISTRADO')

elif opcion == 2: # Read
    lectura_de_datos('registrados.csv')

elif opcion == 3: # Update
    opcion_tres()

elif opcion == 4:
    lectura_de_datos('vendidos.csv')

else:
    try:
        df = pd.read_csv('vendidos.csv')
        suma = df['PRECIO'].sum(axis=0)
        print('Cantidad en soles de autos vendidos: S/ '+str(suma))
    except FileNotFoundError as e:
        print('No se han vendido autos, no hay cantidad en soles.')