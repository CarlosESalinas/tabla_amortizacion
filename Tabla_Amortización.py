import tabulate as tab

def tabla_amor(Prestamo, Interes_anual, Periodo):
  Inter_mensual = (Interes_anual/12)
  Cuota = ((Prestamo * Inter_mensual) / (1 -(1+Inter_mensual)**(Periodo*(-1)))) 
  tabla = []
  Saldo = Prestamo


  for i in range(1,Periodo+1):

    Pago_interes = Saldo * Inter_mensual
    Amortizacion = Cuota - Pago_interes
    Saldo -= Amortizacion
    renglon = [i, format(Cuota, '0,.2f'),
              format(Pago_interes, '0,.2f'), 
              format(Amortizacion, '0,.2f'),
              format(Saldo, '0,.2f')]
    
    tabla.append(renglon)
  print('')
  print('\t\t\t Tabla de amortización')

  return print(tab.tabulate(tabla, 
                    headers = ['Cuota', 
                                'Interés mensual', 
                                'Amortización', 
                                'Saldo'],  
                    tablefmt = 'psql'))

Prestamo = float(input("Ingresa el valor del prestamo: "))
Interes_annual = float(input("Ingresa la tasa de interés anual: "))
Periodo = int(input('Ingresa la cantidad de pagos: '))

resultado = tabla_amor(Prestamo, Interes_annual, Periodo)