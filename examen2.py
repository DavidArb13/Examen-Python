#Conversor de moneda

def moneda1():
    print('        ___________________________________')
    print('        |                                 |')
    print('        |    Conversor de Moneda Daarb    |')
    print('        |         Elija la Monida         |')
    print('        |_________________________________|')
    print('        |                                 |')
    print('        |       1)  Dolar                 |')
    print('        |       2)  Euro                  |')
    print('        |       3)  Yen                   |')
    print('        |       4)  Libra Esterlina       |')
    print('        |       5)  Franco Suiso          |')
    print('        |       6)  Peso Colombiano       |')
    print('        |_________________________________|')

def validacion(mod1):
    while (mod1 <= 0 or mod1 > 6):
        mod1 = int(input('Ingrese moneda Valida a convertir:     '))
    else:
        if mod1 == 1:
            m= 'dolares'
        elif mod1 == 2:
            m= 'Euros'
        elif mod1 == 3:
            m= 'Yenes'
        elif mod1 == 4:
            m= 'Libras Esterlinas'
        elif mod1 == 5:
            m= 'Francos Suizos'
        elif mod1 == 6:
            m= 'Pesos Colombianos'
    return [mod1,m]

def validacion2(mod1,mod2):
    while (mod2 <= 0 or mod2 > 6):
        mod2 = int(input('Ingrese la segunda moneda valida para la Conversion:    '))
    while (mod1 == mod2) or (mod2 <= 0 or mod2 > 6):
        mod2 = int(input('Ingrese la segunda moneda diferente a la inicial y valida para la Conversion:    '))
    return mod2

def nr2(d):
    if d == 1:
        c1= 'dolares'
    elif d == 2:
        c1= 'Euros'
    elif d == 3:
        c1= 'Yenes'
    elif d == 4:
        c1= 'Libras Esterlinas'
    elif d == 5:
        c1= 'Francos Suizos'
    elif d == 6:
        c1= 'Pesos Colombianos'
    return c1

def r(m1,m2,val,tot):
    print(f' _____________________________________________________________________')
    print(f'|  Conversión:                                                        |')
    print(f'|_____________________________________________________________________|')
    print(f'   {m1}                     ${val}                                     ') 
    print(f'   Equivalentes a              ${tot} {m2}                             ')
    print(f' _____________________________________________________________________')

def conversor(val,mod1,mod2,m1,m2):
    #Cop equivalencias
    if mod1 == 6 and mod2 == 1:
        tot= val/3765.00
        r(m1,m2,val,tot)
    elif mod1 == 6 and mod2 == 2:
        tot= val/4427.14
        r(m1,m2,val,tot)
    elif mod1 == 6 and mod2 == 3:
        tot= val/35.15
        r(m1,m2,val,tot)
    elif mod1 == 6 and mod2 == 4:
        tot= val/4896
        r(m1,m2,val,tot)
    elif mod1 == 6 and mod2 == 5:
        tot= val/4117
        r(m1,m2,val,tot)
    #usd equivalencias
    elif mod1 == 1 and mod2 == 2:
        tot= val/1.18
        r(m1,m2,val,tot)
    elif mod1 == 1 and mod2 == 3:
        tot= val*106.64
        r(m1,m2,val,tot)
    elif mod1 == 1 and mod2 == 4:
        tot= val/1.31
        r(m1,m2,val,tot)
    elif mod1 == 1 and mod2 == 5:
        tot= val/1.10
        r(m1,m2,val,tot)
    elif mod1 == 1 and mod2 == 6:
        tot= val/0.00027
        r(m1,m2,val,tot)
    #eur equivalencias
    elif mod1 == 2 and mod2 == 1:
        tot= val/0.85
        r(m1,m2,val,tot)
    elif mod1 == 2 and mod2 == 3:
        tot= val/0.0079
        r(m1,m2,val,tot)
    elif mod1 == 2 and mod2 == 4:
        tot= val/1.11
        r(m1,m2,val,tot)
    elif mod1 == 2 and mod2 == 5:
        tot= val/0.93
        r(m1,m2,val,tot)
    elif mod1 == 2 and mod2 == 6:
        tot= val/0.00023
        r(m1,m2,val,tot)
    #yen equivalencias
    elif mod1 == 3 and mod2 == 1:
        tot= val/106.74
        r(m1,m2,val,tot)
    elif mod1 == 3 and mod2 == 2:
        tot= val/126.04
        r(m1,m2,val,tot)
    elif mod1 == 3 and mod2 == 4:
        tot= val/139.34
        r(m1,m2,val,tot)
    elif mod1 == 3 and mod2 == 5:
        tot= val/117.16
        r(m1,m2,val,tot)
    elif mod1 == 3 and mod2 == 6:
        tot= val/0.029
        r(m1,m2,val,tot)
    #libras esterlinas equivalencias
    elif mod1 == 4 and mod2 == 1:
        tot= val/0.77
        r(m1,m2,val,tot)
    elif mod1 == 4 and mod2 == 2:
        tot= val/0.90
        r(m1,m2,val,tot)
    elif mod1 == 4 and mod2 == 3:
        tot= val/0.0072
        r(m1,m2,val,tot)
    elif mod1 == 4 and mod2 == 5:
        tot= val/0.84
        r(m1,m2,val,tot)
    elif mod1 == 4 and mod2 == 6:
        tot= val/0.00021
        r(m1,m2,val,tot)
    #Francos Suizos equivalencias
    elif mod1 == 5 and mod2 == 1:
        tot= val/0.91
        r(m1,m2,val,tot)
    elif mod1 == 5 and mod2 == 2:
        tot= val/1.08
        r(m1,m2,val,tot)
    elif mod1 == 5 and mod2 == 3:
        tot= val/0.0085
        r(m1,m2,val,tot)
    elif mod1 == 5 and mod2 == 4:
        tot= val/1.19
        r(m1,m2,val,tot)
    elif mod1 == 5 and mod2 == 6:
        tot= val/0.00024
        r(m1,m2,val,tot)


if __name__ == "__main__":
    print('\n\n____________________________________________________')
    print ('|                 Usar Conversor                   |')
    print('|__________________________________________________|')
    conver = str(input('                      |Si|No|                   \n'))
    

    while conver.lower() == 'si':

        moneda1()
        mod1 = int(input('\n Ingrese moneda Inicial a convertir:  '))

        m = validacion(mod1)
        mod1 = m[0]
        m1 = m[1]

        val = int(input(f' Ingrese el valor de {m1} a convertir:  $'))
        
        moneda1()
        mod2 = int(input('\nIngrese la segunda moneda para la Conversion:    '))

        mod2 = validacion2(mod1,mod2)

        m2 = nr2(mod2)

        conversor(val,mod1,mod2,m1,m2)

        print('\n\n____________________________________________________')
        print ('|                 Usar Conversor                   |')
        print('|__________________________________________________|')
        conver = str(input('                      |Si|No|                   \n'))















