# Función para imprimir las opciones (registro, visualizacion, venta):
def comandos():
    opciones = ['VENTA AUTOS','1 Registrar auto','2 Autos disponibles','3 Compra auto', '4 Autos Vendidos','5 Cantidad total en S/ de autos vendidos']
    while True:
        for i in opciones:
            print(i)
        try:
            opcion = validar_datos(int(input('\n\nopcion: ')),1)
            break
        except ValueError as e:
            print('No es una opción. \n')
    return opcion

# Función para validar datos (opción, fabricación, precio):
def validar_datos(valor, tipo):
    while True:
        if tipo == 1:
            if valor < 1 or valor > 5:
                print('Debe ser entre 1 y 5. \n')
                valor = int(input('opcion: '))
            else:
                return valor
        elif tipo == 2:
            if valor < 1886 or valor > 2022:
                print('Debe ser un año posible. Desde 1886 - 2022\n')
                valor = int(input('Fabricacion: '))
            else:
                return valor
        elif tipo == 3:
            if valor < 1:
                print('Debe ser un valor positivo.\n')
                valor = int(input('Precio (S/): '))
            else:
                return valor

# Función para ingrear datos (marca, fabricacion, color, precio, estado):
def ingreso_datos():
    marca = input('\nMarca: ')
    fabricacion = validar_datos(int(input('\nFabricacion: ')),2)
    color = input('\nColor: ')
    precio = validar_datos(round(float(input('\nPrecio (S/): '))),3)

    dicAutos = {'MARCA':marca,
              'FABRICACION':fabricacion,
              'COLOR':color,
              'PRECIO':precio,
              'ESTADO':'disponible'}
    return dicAutos