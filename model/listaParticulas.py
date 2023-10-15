import json
from model.particula import Particula
from model.algoritmos import distancia_euclideana
# listParticulas.py
class ListaParticulas:
    def __init__(self) -> None:
        self.__particulas = [] # Lista de particulas

    def __str__(self):
        return "".join(
            str(p) + "\n" for p in self.__particulas
        )

    # Retorna el numero de particulas que hay en la lista de particulas.
    def __len__(self):
        return (
            len(self.__particulas)
        )

    # Permitimos que las particulas sean iterables
    def __iter__(self):
        self.cont = 0

        return self
    
    # Itera sobre la lista de particulas hasta el ultimo elemento de la lista:
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            
            return particula

        else:
            raise StopIteration # Ya no hay mas elementos en la lista. Parar.

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula) # Metemos la particula a la lista

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for p in self.__particulas:
            print(p) # Llama a __str__ de la clase Particula.

    def abrir(self, ruta):
        try:
            with open(ruta, 'r') as archivo: # Abrimos el archivo
                lista = json.load(archivo) # Leemos su contenido en JSON

                if "origen" in lista[0]:
                    # particulas 2.json
                    for i in lista:
                        particula = Particula(i['id'], i['origen']['x'], i['origen']['y'], i['destino']['x'], i['destino']['y'], i['velocidad'], i['color']['red'], i['color']['green'], i['color']['blue'], distancia_euclideana(i['origen']['x'], i['origen']['y'], i['destino']['x'], i['destino']['y']))

                        self.agregar_final(particula)
                        
                else:
                    # file.json
                    for i in lista:
                        particula = Particula(i['id'], i['origen_x'], i['origen_y'], i['destino_x'], i['destino_y'],
                                            i['velocidad'], i['red'], i['green'], i['blue'],
                                            distancia_euclideana(i['origen_x'], i['origen_y'], i['destino_x'], i['destino_y']))

                        self.agregar_final(particula)

                return 1 # Correcto
        
        except:
            return 0 # Error

    def guardar(self, ruta):
        try:
            with open(ruta, 'w') as archivo: # Abrimos el archivo
                # Convertimos todas las particulas de la lista en formato de diccionario
                lista = [particula.to_dict() for particula in self.__particulas]

                # Finalmente ingresamos la informacion al archivo JSON
                json.dump(lista, archivo, indent=5)

                return 1 # Correcto
        except:
            return 0 # Error

    def ordenar_id(self):
        self.__particulas.sort(key=lambda particula : particula.id)
        
    def ordenar_distancia(self):
        self.__particulas = sorted(self.__particulas, key=lambda particula : float(particula.distancia), reverse=True)
        
    def ordenar_velocidad(self):
        self.__particulas.sort(key=lambda particula : particula.velocidad)