# Ejercicio 3 - Hotel de playa
# Hecho por: Wesly Umanzor, Keyla Canales 

class Habitacion:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Hotel:
    def __init__(self):
        self.habitaciones = [
            Habitacion("Estándar", 100),
            Habitacion("Deluxe", 150),
            Habitacion("Suite", 200)
        ]
        self.servicios_extra = {
            "Piscina": 20,
            "Cancha de Golf": 50
        }

    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for idx, hab in enumerate(self.habitaciones, 1):
            print(f"{idx}. {hab.tipo}: ${hab.precio} por noche")

    def calcular_total(self, habitacion, noches, servicios):
        total_habitacion = habitacion.precio * noches
        total_servicios = sum(self.servicios_extra[s] for s in servicios)
        return total_habitacion + total_servicios

    def emitir_factura(self, cliente, habitacion, noches, servicios):
        total = self.calcular_total(habitacion, noches, servicios)
        print("\n--- Factura ---")
        print(f"Cliente: {cliente.nombre}")
        print(f"Dirección: {cliente.direccion}")
        print(f"Teléfono: {cliente.telefono}")
        print(f"Habitación: {habitacion.tipo}")
        print(f"Noches: {noches}")
        print(f"Servicios adicionales: {', '.join(servicios) if servicios else 'Ninguno'}")
        print(f"Total a pagar: ${total}")
        print("----------------\n")

def main():
    hotel = Hotel()

    # Mostrar las habitaciones disponibles
    hotel.mostrar_habitaciones()

    # Selección de la habitación
    opcion_habitacion = int(input("Seleccione el número de la habitación que desea: ")) - 1
    habitacion_elegida = hotel.habitaciones[opcion_habitacion]

    # Solicitar datos del cliente
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su teléfono: ")
    cliente = Cliente(nombre, direccion, telefono)

    # Número de noches
    noches = int(input("¿Cuántas noches se quedará?: "))

    # Servicios adicionales
    servicios_elegidos = []
    while True:
        print("\nServicios adicionales disponibles:")
        for servicio, costo in hotel.servicios_extra.items():
            print(f"{servicio}: ${costo}")
        servicio = input("Ingrese el nombre del servicio extra (o 'ninguno' para continuar): ").title()
        if servicio == "Ninguno":
            break
        elif servicio in hotel.servicios_extra:
            servicios_elegidos.append(servicio)
        else:
            print("Servicio no válido, inténtelo de nuevo.")

    # Emitir factura
    hotel.emitir_factura(cliente, habitacion_elegida, noches, servicios_elegidos)

if __name__ == "__main__":
    main()
