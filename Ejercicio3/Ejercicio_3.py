# Constantes para los puntos
V = 3  # Victoria
E = 1  # Empate

print('Bienvenido')

# Cantidad de partidos ganados
pg = int(input('Ingrese la cantidad de partidos GANADOS: '))

# Cantidad de partidos empatados
pe = int(input('Ingrese la cantidad de partidos EMPATADOS: '))

# Puntuación total
p = (pg * V) + (pe * E)

print('La puntuación actual de tu equipo es de', p, 'puntos.')