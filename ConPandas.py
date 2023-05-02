import pandas as pd
from funciones import *
def lectura_de_datos(archivo):
    try:
        df = pd.read_csv(archivo)
        df = df.sort_values(by=['MARCA', 'PRECIO'])
        df.to_csv(archivo, mode='w', index=False)
        print(df)
    except FileNotFoundError as e:
        print ('No hay datos para mostrar en '+archivo)

def opcion_tres():
    while True:
        try:
            datos = pd.read_csv('registrados.csv')
            dictUpdate = ingreso_datos()
            m_marca = (datos['MARCA']==dictUpdate['MARCA'])
            m_fabricacion = (datos['FABRICACION']==dictUpdate['FABRICACION'])
            m_color = (datos['COLOR']==dictUpdate['COLOR'])
            m_precio = (datos['PRECIO']==dictUpdate['PRECIO'])
            try:
                encontrado=datos.index[m_marca & m_fabricacion & m_color & m_precio].tolist()
                datos.loc[encontrado[0],'ESTADO']='vendido'
                print(datos)
                dfu = pd.DataFrame(datos.loc[encontrado], columns=['MARCA', 'FABRICACION', 'COLOR', 'PRECIO', 'ESTADO'])
                datos.drop(encontrado, inplace=True)
                datos.to_csv('registrados.csv', index=False)
                print('\n AUTO VENDIDO')
                try:
                    first_read = pd.read_csv('vendidos.csv')
                    dfu.to_csv('vendidos.csv', header=False, mode='a', index=False)
                    break
                except OSError as e:
                    dfu.to_csv('vendidos.csv', mode='a', index=False)
                    break
            except IndexError as e:
                print('Los datos ingresados no existen o no son validos. Por favor, intente nuevamente')
        except FileNotFoundError as e:
            print('No existen autos para vender. Por favor, registre uno.')
            break