# particula.py
class Particula:
    def __init__(self, id = 0, x_o = 0, y_o = 0, x_d = 0, y_d = 0, velocidad = 0, rojo = 0, verde = 0, azul = 0, distancia = 0.0) -> None:
        # Inicializamos variables de la particula
        self.__id = id
        self.__x_o = x_o
        self.__y_o = y_o
        self.__x_d = x_d
        self.__y_d = y_d
        self.__velocidad = velocidad
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
        self.__distancia = distancia

    # Formato personalizado para la impresion de una particula
    def __str__(self) -> str:
        return (
            "ID: " + str(self.__id) + "\n" + 
            "Origen x: " + str(self.__x_o) + "\n" + 
            "Origen y: " + str(self.__y_o) + "\n" + 
            "Destino x: " + str(self.__x_d) + "\n" + 
            "Destino y: " + str(self.__y_d) + "\n" + 
            "Velociad: " + str(self.__velocidad) + "\n" + 
            "Rojo: " + str(self.__rojo) + "\n" + 
            "Verde: " + str(self.__verde) + "\n" + 
            "Azul: " + str(self.__azul) + "\n" + 
            "Distancia: " + str(self.__distancia) + "\n"
        )

    def to_dict(self): # Particula -> Diccionario
        return {
            "id": self.__id,
            "origen_x": self.__x_o,
            "origen_y": self.__y_o,
            "destino_x": self.__x_d,
            "destino_y": self.__y_d,
            "velocidad": self.__velocidad,
            "red": self.__rojo,
            "green": self.__verde,
            "blue": self.__azul
        }
    
    def __lt__(self, other):
        return self.__id < other.__id

    @property
    def id(self):
        return self.__id
    @property
    def origen_x(self):
        return self.__x_o
    @property
    def origen_y(self):
        return self.__y_o
    @property
    def destino_x(self):
        return self.__x_d
    @property
    def destino_y(self):
        return self.__y_d
    @property
    def velocidad(self):
        return self.__velocidad
    @property
    def rojo(self):
        return self.__rojo
    @property
    def verde(self):
        return self.__verde
    @property
    def azul(self):
        return self.__azul
    @property
    def distancia(self):
        return self.__distancia