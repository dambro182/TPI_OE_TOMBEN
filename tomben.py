def enlistar_datos():
    with open('db.csv', 'r') as archivo: #abrimos el archivo en modo read
            empleados = []
            archivo.readline() # saltamos encabezado
            for linea in archivo: #leemos linea por linea
                linea_limpia = linea.strip()
                legajo, nombre, dias_disponibles = linea_limpia.split(',') #desempaquetamos la linea
                legajo = int(legajo)
                empleado = {
                    'legajo' : int(legajo),
                    'nombre' : nombre,
                    'dias_disp' : int(dias_disponibles),
                }
                empleados.append(empleado)
    return empleados


def solicitar_vacaciones(lista_empleados):
    print('Bienvenido al sistema de solicitud de vacaciones de TomBen.')
    print('A continuación se verificará su saldo de días disponibles.')
    while True:
        legajo_existente = None
        
        try:
            legajo = int(input('Legajo: '))
        except ValueError:
            print('Error. Ingrese un numero valido.')
            continue
        
        for empleado in lista_empleados:
            if legajo == empleado['legajo']:
                legajo_existente = empleado['legajo']
                nombre_empleado = empleado['nombre']
                dias_empleado = empleado['dias_disp']
                break
        
        if legajo_existente is None:
            print('Error. No se encuentra ningun empleado con ese numero de legajo.')
            continue
        break
    
    print(f'Bienvenido {nombre_empleado}, a continuacion ingrese cuantos dias de vacaciones le gustaria solicitar.')
    while True:
        try:
            dias_solicitados = int(input('Dias solicitados: '))
        except ValueError:
            print('Error. Ingrese un numero valido.')
            continue
        
        if dias_solicitados <= 0:
            print('No puede solicitar dias negativos.') 
            continue
        
        if dias_solicitados > dias_empleado:
            print(f'Saldo insuficiente. Usted solo cuenta con {dias_empleado} día/s disponibles.')
            print(f'No es posible procesar una solicitud de {dias_solicitados} día/s.')
            continue
        
        elif dias_solicitados <= dias_empleado:
            for empleado in lista_empleados:
                if legajo == empleado['legajo']:
                    empleado['dias_disp'] = empleado['dias_disp'] - dias_solicitados
            
            print(f'Verificación exitosa. Usted cuenta con saldo suficiente para {dias_solicitados} día/s.')
            print(f'Su solicitud ha sido registrada. Días restantes: {dias_empleado - dias_solicitados}. Saludos, TomBen Chatbot.')
            break
        else:
            print('Errorr.')
            continue

def actualizar_datos(lista_empleados):
    with open('db.csv', 'w') as archivo: #abrimos el archivo en modo write
        
            archivo.write('legajo,nombre,dias disponibles\n')
            
            for empleado in lista_empleados:
                archivo.write(
                    f"{empleado['legajo']},"
                    f"{empleado['nombre']},"
                    f"{empleado['dias_disp']}\n"
                )

empleados = enlistar_datos()
solicitar_vacaciones(empleados)
actualizar_datos(empleados)