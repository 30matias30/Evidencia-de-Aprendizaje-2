# Definimos las constantes
LECHE = 1000
D = 0.10
D2 = 0.15
DJ = 0.10
MNT_MIN = 12
MNT_MAX = 24
J = 'y'

# cantidad de leches
print('Bienvenido a la LECHERIA, ¿cuántas leches va a llevar?')
cL = int(input('Cantidad: '))

# Cálculo del precio base (pB)
pB = cL * LECHE

# Cálculo del descuento (si corresponde)
if cL > MNT_MIN and cL <= MNT_MAX:
    desc = pB * D 
else:
    if cL > MNT_MAX:
        desc = pB * D2
    else:
        print('La cantidad no llega al monto de mayorista')
        desc = 0

#  Es jubilado?
print('¿Eres JUBILADO? (y/n)')
rJ = input()

# descuento para jubilados
if rJ == J:
    descJ = pB * DJ
    pF = pB - desc - descJ
else:
    pF = pB - desc

# Imprime el precio final de la compra
print('El precio final de tu compra láctea es de:')
print('$', pF)
