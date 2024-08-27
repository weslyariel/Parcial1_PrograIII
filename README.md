este es nuestro repositorio y grupo de trabajo para el parcial.
Estudiantes:
Wesly Ariel Umanzor Arias - SMTR072723
Keila Nallely Canales Nuñez - SMTR068223


EJERCICIO 1
Razonamiento:
Uso de Programación Orientada a Objetos (POO):
Clases Utilizadas:
Producto: Representa los productos con nombre y precio.
Inventario: Maneja el inventario de productos, permitiendo agregar, eliminar y mostrar productos.
Proveedor: Simula la entrega de productos al inventario.
Cliente: Realiza compras, calculando el total y el vuelto, y actualiza el inventario.
Justificación del Uso de POO:
Modularidad y Encapsulación: Cada clase tiene una responsabilidad específica, lo que mejora la organización del código y facilita el mantenimiento.
Escalabilidad: La implementación modular permite añadir nuevas funcionalidades fácilmente, como la gestión de descuentos o promociones.

Funcionalidades de Python Utilizadas:
Entrada de Datos: La función input () se utiliza para interactuar con el usuario, permitiendo registrar productos y realizar compras.
Manejo de Errores: Se implementan excepciones (ValueError) para manejar casos como falta de inventario o dinero insuficiente.

Decisión de Implementación:
Entrada de Datos desde Consola: Permite simular el proceso de agregar productos al inventario y realizar compras de manera interactiva.
Estructura de Datos: Se utiliza un diccionario en Inventario para una gestión eficiente de productos y sus cantidades, permitiendo búsquedas rápidas y actualizaciones precisas.




EJERCICIO 2
Razonamiento:
Uso de Programación Orientada a Objetos (POO):
Clases Utilizadas:
Estudiante: Representa a un estudiante con un historial de asistencia. Permite registrar y mostrar la asistencia.
Docente: Representa a un docente que puede agregar estudiantes y registrar su asistencia.
Director: Representa al director que puede revisar el registro de asistencia de todos los estudiantes bajo el control del docente.
Justificación del Uso de POO:
Modularidad y Encapsulación: Cada clase tiene una responsabilidad específica, lo que hace que el código sea más organizado y fácil de mantener.
Escalabilidad: El sistema es fácil de extender con nuevas funcionalidades, como generar reportes o manejar múltiples docentes.

Funcionalidades de Python Utilizadas:
Entrada de Datos: Utilizamos input() para permitir la entrada de datos desde el usuario, facilitando la interacción.
Gestión de Fechas: Usamos el módulo datetime para manejar fechas, lo que permite registrar la asistencia en fechas específicas.
Estructura de Datos: Utilizamos listas y diccionarios para almacenar y gestionar la asistencia y los estudiantes de manera eficiente.


Decisión de Implementación:
Registro de Asistencia: Cada estudiante tiene un historial de asistencia que se actualiza con cada nuevo registro.
Razón de Permiso: Se incluye un campo opcional para registrar la razón del permiso, que solo se solicita si el estado es "permiso".
Revisión por el director: El director puede revisar toda la asistencia registrada para cada estudiante, permitiendo un control y seguimiento efectivo.


