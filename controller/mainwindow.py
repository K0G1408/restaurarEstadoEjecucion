from PySide2.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog, QMessageBox, QTableWidgetItem
from view.mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from random import randint
from model.particula import Particula
from model.listaParticulas import ListaParticulas
from model.algoritmos import distancia_euclideana, get_puntos, puntos_mas_cercanos
from pprint import pprint
import datetime, prefect
#import threading, time

class MainWindow(QMainWindow):

    def timer(self): # REALIZA LA ACCION DE RESPALDO CADA 1 MINUTO #
        while True: # Accion a repetir
            self.action_guardar_archivo_respaldo()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.puntos = [] # Lista de puntos
        self.particulas = ListaParticulas() # Instancia a la clase ListaParticulas
        self.diccionario = dict() # Diccionario para representar el grafo
        
        # Iniciar la ejecución en segundo plano.
        #t = threading.Thread(target = self.timer)
        #t.start()

        # USAMOS PREFECT PARA PROGRAMAR UNA COPIA DE SEGURIDAD #
        schedule = IntervalSchedule(interval=datetime.timedelta(minutes=1))

        with Flow("My flow", schedule) as F:
            self.timer()
        
        f.run()


        self.__id  = 0
        self.__origen_x  = 0
        self.__origen_y  = 0
        self.__destino_x  = 0
        self.__destino_y  = 0
        self.__velocidad  = 0
        self.__rojo  = 0
        self.__verde  = 0
        self.__azul  = 0
        self.__distancia  = 0

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)
        self.ui.agregar_final.clicked.connect(self.agregar_final)
        self.ui.agregar_inicio.clicked.connect(self.agregar_inicio)
        self.ui.mostrar.clicked.connect(self.mostrar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # Abrir / Guardar archivo
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        # Mostrar tabla:
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        # Buscar en la tabla:
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        # Ordenar
        self.ui.ordenar_id.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad.clicked.connect(self.ordenar_velocidad)

        # Puntos y fuerza bruta
        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
        self.ui.actionPuntos_Cercanos.triggered.connect(self.mostrar_puntos_cercanos)

        # Mostrar lista de adyacencias del grafo
        self.ui.mostrar_adyacencias.clicked.connect(self.mostrar_adyacencias)
        
    @Slot()
    def action_guardar_archivo_respaldo(self): # GUARDA ARCHIVO DE RESPALDO #
        print("Respaldado")
        self.particulas.guardar("C:/SEMINARIO DE ALGORITMIA/ACT10/model/respaldo.json")

    # Creamos un evento para ampliar el grafico de particulas dependiendo el scroll que haga el usuario
    def wheelEvent(self, event): # Se "manda a llamar" cuando el usuario hace scroll en el mouse.
        #print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    def crear_diccionario(self):
        # Llenamos diccionario de datos:
        for particula in self.particulas:
            # Tomamos origen (key) de la particula (x, y):
            key = (particula.origen_x, particula.origen_y)
            
            # Tomamos (value) de la particula (x, y):
            value = [(particula.destino_x, particula.destino_y), particula.distancia]

            # Verificamos si la llave (origen) ya existe en el diccionario:
            if key in self.diccionario:
                # Metemos "value" como una lista en la lista de la llave "key"
                self.diccionario[key].append(value)
            else:
                # Metemos nodo (key) y arista (value) al diccionario:
                self.diccionario[key] = [value]

            #pprint(self.diccionario)

    @Slot()
    def mostrar_adyacencias(self):
        # Creamos diccionario
        self.crear_diccionario()
        print(self.diccionario)

        # Iteramos sobre el diccionario:
        resultado = ""
        for key, value in self.diccionario.items():
            # Eliminamos el peso de cada nodo adyacente:
            adyacentes = []
            for adyacente in value:
                del adyacente[-1]
                adyacentes.append(adyacente) # Añadimos lista a la lista sin pesos

            # Imprimimos lista de adyacencias:
            resultado = resultado + str(key) + "-->" + str(adyacentes) + "\n"

        # Finalmente mostramos resultado en pantalla
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(resultado)

    @Slot()
    def mostrar_puntos_cercanos(self):
        self.scene.clear()
        self.puntos = get_puntos(self.particulas)
        resultado = puntos_mas_cercanos(self.puntos)
        
        for punto1, punto2, color in resultado:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]

            # Damos estilos.
            pen = QPen()
            pen.setWidth(2)
            color = QColor(color[0], color[1], color[2])
            pen.setColor(color)

            self.scene.addEllipse(x1, y1, 6, 6, pen) # Imprimimos puntos en pantalla
            self.scene.addEllipse(x2, y2, 6, 6, pen)

            self.scene.addLine(x1+3, y1+3, x2+3, y2+3, pen) # Unimos puntos obtenidos mediante una linea recta

    @Slot()
    def dibujar_puntos(self):
        self.puntos = get_puntos(self.particulas)

        # Obtenemos los puntos de las particulas ya cargadas
        self.scene.clear()

        for punto in self.puntos:
            # Obtenemos puntos
            o_x = punto[0][0]
            o_y = punto[0][1]
            d_x = punto[1][0]
            d_y = punto[1][1]
        
            # Damos estilos.
            pen = QPen()
            pen.setWidth(2)
            color = QColor(punto[2][0], punto[2][1], punto[2][2])
            pen.setColor(color)

            self.scene.addEllipse(o_x, o_y, 6, 6, pen) # Imprimimos puntos en pantalla
            self.scene.addEllipse(d_x, d_y, 6, 6, pen)

    def obtener_datos(self):
        self.__id = self.ui.id.value()
        self.__origen_x = self.ui.origen_x.value()
        self.__origen_y = self.ui.origen_y.value()
        self.__destino_x = self.ui.destino_x.value()
        self.__destino_y = self.ui.destino_y.value()
        self.__velocidad = self.ui.velocidad.value()
        self.__rojo = self.ui.rojo.value()
        self.__verde = self.ui.verde.value()
        self.__azul = self.ui.azul.value()

        # Calculamos distancia euclideana del origen y destino
        self.__distancia = distancia_euclideana(self.__origen_x, self.__origen_y, self.__destino_x, self.__destino_y)

    
    def obtener_datos_lista(self):
        for particula in self.particulas:
            
            self.__id = int(particula.id)
            self.__origen_x = int(particula.origen_x)
            self.__origen_y = int(particula.origen_y)
            self.__destino_x = int(particula.destino_x)
            self.__destino_y = int(particula.destino_y)
            self.__velocidad = int(particula.velocidad)
            self.__rojo = int(particula.rojo)
            self.__verde = int(particula.verde)
            self.__azul = int(particula.azul)

            # Calculamos distancia euclideana del origen y destino
            self.__distancia = distancia_euclideana(self.__origen_x, self.__origen_y, self.__destino_x, self.__destino_y)

            self.dibujar(True) # Imprimimos particula en pantalla

    @Slot()
    def action_abrir_archivo(self):
        # Obtenemos ruta de archivo
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]
        # Intentamos abrirlo para extraer su contenido
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Correcto",
                "El archivo se abrió correctamente, " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "Hubo un error al intentar abrir el archivo en la ruta: " + ubicacion
            )
    
        # Imprimimos particulas en pantalla
        self.obtener_datos_lista()
        
    @Slot()
    def action_guardar_archivo(self):
        # Obtenemos ruta de archivo
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            '.',
            'JSON (*.json)'
        )[0]
        # Intentamos abrirlo para guardar el contenido actual de las particulas
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Correcto",
                "El archivo se guardó correctamente en la ruta: " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "Hubo un error al intentar guardar el archivo en la ruta: " + ubicacion
            )

    @Slot()
    def agregar_final(self): # Obtenemos los valores ingresados por el usuario
        self.obtener_datos()

        # Creamos objeto particula a partir de los datos obtenidosa arriba
        particula = Particula(self.__id, self.__origen_x, self.__origen_y, self.__destino_x, 
                                self.__destino_y, self.__velocidad, self.__rojo, self.__verde, 
                                self.__azul, self.__distancia)

        # Añadimos particula a la lista de particulas
        self.particulas.agregar_final(particula)
        
    @Slot()
    def agregar_inicio(self):
        self.obtener_datos()

        # Creamos objeto particula a partir de los datos obtenidosa arriba
        particula = Particula(self.__id, self.__origen_x, self.__origen_y, self.__destino_x, 
                                self.__destino_y, self.__velocidad, self.__rojo, self.__verde, 
                                self.__azul, self.__distancia)

        # Añadimos particula a la lista de particulas
        self.particulas.agregar_inicio(particula)
    
    @Slot()
    def mostrar(self):
        # Limpiamos datos en pantalla
        self.ui.plainTextEdit.clear()
        # Obtenemos lista de particulas como string y lo mostramos en pantalla.
        self.ui.plainTextEdit.insertPlainText(str(self.particulas))


    @Slot()
    def dibujar(self, abrir = False):
        #print("dibujar")
        # Damos estilos a los elementos del gráfico
        pen = QPen()
        pen.setWidth(2)

        # Obtenemos los valores ingresados por el usuario
        if not abrir:
            self.obtener_datos()
        
        # Generamos particulas a partir de los valores ingresados por el usuario
        color = QColor(self.__rojo, self.__verde, self.__azul)
        pen.setColor(color)

        self.scene.addEllipse(self.__origen_x, self.__origen_y, 6, 6, pen)
        self.scene.addEllipse(self.__destino_x, self.__destino_y, 6, 6, pen)

        # Unimos ambos puntos creados mediante una recta
        self.scene.addLine(self.__origen_x+3, self.__origen_y+3, self.__destino_x+3, self.__destino_y+3, pen)
        
    @Slot()
    def limpiar(self):
        #print("limpiar")
        self.scene.clear()
        self.ui.graphicsView.setTransform(QTransform())

    @Slot()
    def mostrar_tabla(self):
        # Creamos columnas de la tabla:
        self.ui.tabla.setColumnCount(10)
        # Creamos su encabezado:
        headers = ["ID", "Origen x", "Destino x", "Origen y", "Destino y", "Velocidad", "Rojo", "Verde", "Azul", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        # Ingresamos el numero de columnas que tendra la tabla:
        # Basado en el numero de particulas de la clase listaParticulas.
        self.ui.tabla.setRowCount(len(self.particulas))

        # Recorremos las particulas de la lista de particulas y las mostramos en la tabla
        row = 0 # Inicializamos la fila en 0
        for particula in self.particulas:
            # Obtenemos los atributos de la particula obtenida:
            id = QTableWidgetItem(str(particula.id))
            origen_x = QTableWidgetItem(str(particula.origen_x))
            origen_y = QTableWidgetItem(str(particula.origen_y))
            destino_x = QTableWidgetItem(str(particula.destino_x))
            destino_y = QTableWidgetItem(str(particula.destino_y))
            velocidad = QTableWidgetItem(str(particula.velocidad))
            rojo = QTableWidgetItem(str(particula.rojo))
            verde = QTableWidgetItem(str(particula.verde))
            azul = QTableWidgetItem(str(particula.azul))
            distancia = QTableWidgetItem(str(distancia_euclideana(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y)))

            # Añadimos particula a la tabla (row, column, data):
            self.ui.tabla.setItem(row, 0, id)
            self.ui.tabla.setItem(row, 1, origen_x)
            self.ui.tabla.setItem(row, 2, origen_y)
            self.ui.tabla.setItem(row, 3, destino_x)
            self.ui.tabla.setItem(row, 4, destino_y)
            self.ui.tabla.setItem(row, 5, velocidad)
            self.ui.tabla.setItem(row, 6, rojo)
            self.ui.tabla.setItem(row, 7, verde)
            self.ui.tabla.setItem(row, 8, azul)
            self.ui.tabla.setItem(row, 9, distancia)

            row += 1 # Incrementamos la fila de la tabla en 1

    @Slot()
    def buscar_id(self):
        #print("Buscar")
        # Obtenemos el ID ingresado
        id = self.ui.buscar_lineEdit.text()

        # Hacemos una busqueda lineal del registro que se desea obtener:
        encontrado = False
        for particula in self.particulas:
            if id == str(particula.id): # Elemento encontrado
                # Limpiamos la tabla actual:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                # Obtenemos los atributos de la particula obtenida:
                id = QTableWidgetItem(str(particula.id))
                origen_x = QTableWidgetItem(str(particula.origen_x))
                origen_y = QTableWidgetItem(str(particula.origen_y))
                destino_x = QTableWidgetItem(str(particula.destino_x))
                destino_y = QTableWidgetItem(str(particula.destino_y))
                velocidad = QTableWidgetItem(str(particula.velocidad))
                rojo = QTableWidgetItem(str(particula.rojo))
                verde = QTableWidgetItem(str(particula.verde))
                azul = QTableWidgetItem(str(particula.azul))
                distancia = QTableWidgetItem(str(distancia_euclideana(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y)))

                # Añadimos particula a la tabla (row, column, data):
                self.ui.tabla.setItem(0, 0, id)
                self.ui.tabla.setItem(0, 1, origen_x)
                self.ui.tabla.setItem(0, 2, origen_y)
                self.ui.tabla.setItem(0, 3, destino_x)
                self.ui.tabla.setItem(0, 4, destino_y)
                self.ui.tabla.setItem(0, 5, velocidad)
                self.ui.tabla.setItem(0, 6, rojo)
                self.ui.tabla.setItem(0, 7, verde)
                self.ui.tabla.setItem(0, 8, azul)
                self.ui.tabla.setItem(0, 9, distancia)

                encontrado = True
                return
            
        if not encontrado: # Si el vuelo no se encontro
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula con identificador {id} no fue encontrada'
            )
            
    @Slot()
    def ordenar_id(self):
        self.particulas.ordenar_id()

    @Slot()
    def ordenar_distancia(self):
        self.particulas.ordenar_distancia()

    @Slot()
    def ordenar_velocidad(self):
        self.particulas.ordenar_velocidad()