# Definimos la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Definimos la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]['cantidad'] += cantidad
        else:
            self.productos[producto.nombre] = {'producto': producto, 'cantidad': cantidad}
    
    def eliminar_producto(self, producto, cantidad):
        if producto.nombre in self.productos and self.productos[producto.nombre]['cantidad'] >= cantidad:
            self.productos[producto.nombre]['cantidad'] -= cantidad
            if self.productos[producto.nombre]['cantidad'] == 0:
                del self.productos[producto.nombre]
        else:
            raise ValueError("No hay suficiente cantidad de producto en inventario.")
    
    def mostrar_inventario(self):
        print("Inventario actual:")
        for item in self.productos.values():
            prod = item['producto']
            print(f"{prod.nombre}: ${prod.precio:.2f} - Cantidad: {item['cantidad']}")

# Definimos la clase Proveedor
class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def entregar_producto(self, inventario, producto, cantidad):
        inventario.agregar_producto(producto, cantidad)

# Definimos la clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def realizar_compra(self, inventario, productos_compra, dinero_entregado):
        total_compra = 0
        for producto, cantidad in productos_compra.items():
            if producto.nombre in inventario.productos and inventario.productos[producto.nombre]['cantidad'] >= cantidad:
                total_compra += cantidad * producto.precio
            else:
                raise ValueError(f"No hay suficiente cantidad de {producto.nombre} en inventario.")
        
        vuelto = dinero_entregado - total_compra
        if vuelto < 0:
            raise ValueError("El dinero entregado no es suficiente para cubrir la compra.")
        
        for producto, cantidad in productos_compra.items():
            inventario.eliminar_producto(producto, cantidad)
        
        return total_compra, vuelto

# Función principal para interactuar con el usuario
def main():
    inventario = Inventario()
    
    # Parte 1: Registrar productos del proveedor
    print("Registro de productos del proveedor")
    proveedor_nombre = input("Ingrese el nombre del proveedor: ")
    proveedor = Proveedor(proveedor_nombre)
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        precio_producto = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        
        producto = Producto(nombre_producto, precio_producto)
        proveedor.entregar_producto(inventario, producto, cantidad_producto)
    
    inventario.mostrar_inventario()
    
    # Parte 2: Registrar compra del cliente
    print("\nRegistro de compra del cliente")
    cliente_nombre = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(cliente_nombre)
    
    productos_compra = {}
    while True:
        nombre_producto = input("Ingrese el nombre del producto que desea comprar (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        
        if nombre_producto in inventario.productos:
            producto = inventario.productos[nombre_producto]['producto']
            productos_compra[producto] = cantidad_producto
        else:
            print(f"El producto {nombre_producto} no está en inventario.")
    
    dinero_entregado = float(input("Ingrese el dinero entregado por el cliente: "))
    
    try:
        total_compra, vuelto = cliente.realizar_compra(inventario, productos_compra, dinero_entregado)
        print(f"\nTotal de compra: ${total_compra:.2f}")
        print(f"Vuelto: ${vuelto:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    
    inventario.mostrar_inventario()

if __name__ == "__main__":
    main()

