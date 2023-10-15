# algoritmos.py
import math

def distancia_euclideana(origen_x, origen_y, destino_x, destino_y) -> int:
    # Calculamos la distancia entre los dos puntos
    distancia = math.sqrt(pow(destino_x - origen_x, 2) + pow(destino_y - origen_y, 2))

    return distancia

def get_puntos(particulas : list) -> list:
    puntos = [] # Lista de tuplas, cada tupla tiene un x y un y

    for punto in particulas:
        #x = randint(0, 500)
        #y = randint(0, 500)
        
        # Obtenemos puntos
        o_x = punto.origen_x
        o_y = punto.origen_y
        d_x = punto.destino_x
        d_y = punto.destino_y
        c = (punto.rojo, punto.verde, punto.azul)

        punto = ((o_x, o_y), (d_x, d_y), c) # Creamos un punto, con los valores aleatorios x e y.
        puntos.append(punto) # Añadimos puntos a la lista

    return puntos # Retornamos lista de puntos

def puntos_mas_cercanos(puntos_list) -> list:
    resultado = [] # Lista de tuplas

    for punto_i in puntos_list:
        x1 = punto_i[0][0] # Tomamos un punto de "origen"
        y1 = punto_i[0][1]

        min = 1000
        cercano = (0, 0)
        
        for punto_j in puntos_list:
            if (x1, y1) != (punto_j[0][0], punto_j[0][1]): # Que no se compare consigo mismo como origen
                x2 = punto_j[0][0] # Tomamos otro punto de "origen"
                y2 = punto_j[0][1]
                d = distancia_euclideana(x1, y1, x2, y2) # Tomamos su distancia
                if d < min: # Comparamos distancias para encontrar una minima
                    min = d
                    cercano = (x2, y2)

            # Pero que si se compare con todos los destinos
            x2 = punto_j[1][0]
            y2 = punto_j[1][1]
            d = distancia_euclideana(x1, y1, x2, y2) # Tomamos su distancia
            if d < min: # Comparamos distancias para encontrar una minima
                min = d
                cercano = (x2, y2) # Volvemos a actualizar minimo, en caso de ser necesario.

        resultado.append(((x1, y1), cercano, punto_i[2])) # Origen, destino, color


    # Mismo caso para destinos
    for punto_i in puntos_list:
        x1 = punto_i[1][0]
        y1 = punto_i[1][1]

        min = 10000
        cercano = (0, 0)
        
        for punto_j in puntos_list:
            # Que se compare con todos los origenes
            x2 = punto_j[0][0]
            y2 = punto_j[0][1]
            d = distancia_euclideana(x1, y1, x2, y2) # Tomamos su distancia
            if d < min: # Comparamos distancias para encontrar una minima
                min = d
                cercano = (x2, y2)

            # Y con todos los destinos, a excepcion de si mismo
            if (x1, y1) != (punto_j[1][0], punto_j[1][1]):
                # Comparamos con el punto destino del punto j-esimo.
                x2 = punto_j[1][0]
                y2 = punto_j[1][1]
                d = distancia_euclideana(x1, y1, x2, y2) # Tomamos su distancia
                if d < min: # Comparamos distancias para encontrar una minima
                    min = d
                    cercano = (x2, y2) # Volvemos a actualizar minimo, en caso de ser necesario.

        resultado.append(((x1, y1), cercano, punto_i[2])) # Origen, destino, color
  
    return resultado # Retornamos lista con los puntos y sus distancias minimas con respecto a los demas puntos

