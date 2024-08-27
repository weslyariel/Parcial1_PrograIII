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


Explicación y Análisis del problema:
Ejercicio # 3 – Hotel de playa.
Uso de Programación Orientada a Objetos (POO):
Decidimos utilizar La programación orientada a objetos en este ejercicio porque permite modelar entidades que a nuestro parecer son reales (hotel, habitación, cliente). Esto nos facilita el mantenimiento del código, además de reflejar bien la relación entre las entidades.
Nosotros decidimos crear tres clases principales las cuales son:
Habitación: Este representa una habitación en el hotel, con tipo y precio.
Cliente: Contiene los datos personales del cliente (nombre, dirección y teléfono).
Hotel: Busca gestionar las habitaciones disponibles, los servicios adicionales y emite las facturas.

Estas clases encapsulan la lógica correspondiente, lo que mejora la modularidad y la reutilización del código.
Interactividad del Programa:
El programa interactúa con el usuario solicitando la selección de la habitación, los datos del cliente, el número de noches y los servicios adicionales.
Decidimos por un ciclo while que permite al usuario agregar múltiples servicios adicionales hasta que decida continuar sin más adiciones.

Emisión de Factura:
La factura detallada incluye la información del cliente, la habitación que se seleccione el número de noches, los servicios adicionales y el total a pagar.
La lógica de cálculo del total está separada en el método calcular total para facilitar la comprensión y modificación si fuera necesario.

Justificación del Enfoque:
El uso de POO es beneficioso para este ejercicio porque permite que cada entidad tenga sus propias responsabilidades bien definidas, lo que simplifica futuras modificaciones, como agregar más tipos de habitaciones o servicios adicionales sin afectar el flujo principal del programa.

Explicación y Análisis del problema:
Ejercicio # 4 – Una empresa cuenta con dos tipos de empleados
En esta ocasión decidimos utilizar solo funciones para el programa ya que observamos que de esta manera se nos hizo mas fácil guardar los datos, como el salario base, inicializando ese desde el principio para después mostrarlo al usuario.
Explicación del Razonamiento:
1.	Salario Base Definido:
o	El salario base para los empleados de plaza fija ahora está predefinido como 360 en la función calcular_pago_empleado_fijo, por lo que no se solicita como entrada al usuario.
o	El resto de la lógica permanece igual, con la posibilidad de ingresar las comisiones y años trabajados.
2.	Cálculo de Pagos:
o	La función calcular_pago_empleado_fijo ahora usa el salario base fijo y añade las comisiones y el bono (si corresponde).
o	La función calcular_pago_empleado_por_horas no se ve afectada por este cambio y sigue calculando el pago en función de las horas trabajadas y la tarifa por hora.
Este enfoque garantiza que los empleados de plaza fija siempre reciban un salario base de 360, simplificando el proceso de cálculo.





