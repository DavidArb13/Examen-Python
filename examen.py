'''
David Daniel Arboleda Tolosa
Grupo Nro 2
Albeiro Muriel
Examen Momento 2 Evaluacion ciclo y condicionales
'''

nombre = str(input('Ingrese Nombre del Esclavo: '))
salario = int(input('Ingrese el salario del Esclavo: '))
he = int(input('Ingrese horas extra: '))
hed = int(input('Ingrese horas dominicales: '))

valordia = (salario/30)
valorhora = (salario/240) 

valorhe = (valorhora*0.35)+valorhora
valorhed = (valorhora*0.75)+valorhora

valhetot = (valorhe*he)
valhedtot = (valorhed*hed)

totext = (valhedtot+valhetot)
total = (salario+totext)

print('****************************************************************')
print('                            NOMINA                              ')
print('****************************************************************')

print(f'\nEmpleado                              Sr@{nombre}')
print(f'Salario                                   ${salario:10.1f}')
print(f'Valor x dia                               ${valordia:10.1f}')
print(f'Valor x hora                              ${valorhora:10.1f}')

print('\n____________________________________________________________\n')

print(f'Valor hora extra                          ${valorhe:10.1f}')
print(f'Horas extra                               ${he:10.1f}')
print(f'Valor total horas extra                   ${valhetot:10.1f}')
print(f'Horas dominicales                         ${hed:10.1f}')
print(f'Valor hora extra dominical                ${valorhed:10.1f}')
print(f'Valor total horas extra dominicales       ${valhedtot:10.1f}')

print('\n____________________________________________________________\n')

print(f'Total Extras                              ${totext:10.1f}')
print(f'Total a pagar                             ${total:10.1f}\n')

print('***************************************************************************************')
print('                                     INFORMACION                                       ')
print('*************************************************************************************\n')
if total < 1000000:
    print(f'Sr@ {nombre} Solicita aumento.')
elif total < 2000000:
    ret = total*0.01
    total = total-ret
    print(f'Sr@ {nombre} su salario es de ${total:10.1f} y la retencion es de ${ret:10.1f}.')
elif total <= 3000000:
    ret = total*0.03
    total = total-ret
    print(f'Sr@ {nombre} su salario es de ${total:10.1f} y la retencion es de ${ret:10.1f}.')
elif total > 3000000:
    ret = total*0.04
    total = total-ret
    print(f'Sr@ {nombre} su salario es de ${total:10.1f} y la retencion es de ${ret:10.1f}.\n')

print('****************************************************************************************')
