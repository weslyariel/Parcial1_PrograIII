from datetime import datetime

# Definimos la clase Estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencia = []

    def registrar_asistencia(self, fecha, estado, razon=None):
        self.asistencia.append({
            'fecha': fecha,
            'estado': estado,
            'razon': razon
        })

    def mostrar_asistencia(self):
        print(f"Registro de asistencia para {self.nombre}:")
        for registro in self.asistencia:
            fecha = registro['fecha']
            estado = registro['estado']
            razon = registro.get('razon', 'N/A')
            print(f"Fecha: {fecha}, Estado: {estado}, Razón: {razon}")

# Definimos la clase Docente
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {}

    def agregar_estudiante(self, estudiante):
        self.estudiantes[estudiante.nombre] = estudiante

    def registrar_asistencia(self, nombre_estudiante, fecha, estado, razon=None):
        if nombre_estudiante in self.estudiantes:
            self.estudiantes[nombre_estudiante].registrar_asistencia(fecha, estado, razon)
        else:
            print(f"Estudiante {nombre_estudiante} no encontrado.")

# Definimos la clase Director
class Director:
    def __init__(self, nombre):
        self.nombre = nombre

    def revisar_asistencia(self, docente):
        print(f"\nAsistencia reportada por el docente {docente.nombre}:")
        for estudiante in docente.estudiantes.values():
            estudiante.mostrar_asistencia()

# Función principal para interactuar con el usuario
def main():
    # Crear instancias de Docente y Director
    docente_nombre = input("Ingrese el nombre del docente: ")
    docente = Docente(docente_nombre)
    
    director_nombre = input("Ingrese el nombre del director: ")
    director = Director(director_nombre)

    # Registrar estudiantes
    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre_estudiante.lower() == 'fin':
            break
        estudiante = Estudiante(nombre_estudiante)
        docente.agregar_estudiante(estudiante)

    # Registrar asistencia
    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante para registrar asistencia (o 'fin' para terminar): ")
        if nombre_estudiante.lower() == 'fin':
            break
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        estado = input("Ingrese el estado (asistido, permiso, inasistencia): ").lower()
        razon = None
        if estado == 'permiso':
            razon = input("Ingrese la razón del permiso: ")
        docente.registrar_asistencia(nombre_estudiante, fecha, estado, razon)
    
    # Revisar asistencia por el director
    director.revisar_asistencia(docente)

if __name__ == "__main__":
    main()
