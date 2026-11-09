from base_datos import BaseDatos
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escribe un número.")


def mostrar_menu():
    print("\n===== INVENTARIO DE VIDEOJUEGOS =====")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")


def main():
    base_datos = BaseDatos()
    dao = ProductoDAO(base_datos)
    servicio = ProductoServicio(dao)

    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = leer_entero("Elige una opción: ")

        try:
            if opcion == 1:
                nombre = input("Nombre: ")
                precio = leer_decimal("Precio: ")
                stock = leer_entero("Cantidad disponible: ")
                servicio.registrar(nombre, precio, stock)
                print("Videojuego guardado correctamente.")

            elif opcion == 2:
                productos = servicio.listar()
                if len(productos) == 0:
                    print("El inventario está vacío.")
                else:
                    for p in productos:
                        print(f"ID: {p.id} | {p.nombre} | "
                              f"Precio: ${p.precio:,.0f} | Stock: {p.stock}")

            elif opcion == 3:
                id = leer_entero("ID a buscar: ")
                p = servicio.buscar(id)
                print(f"ID: {p.id} | {p.nombre} | "
                      f"Precio: ${p.precio:,.0f} | Stock: {p.stock}")

            elif opcion == 4:
                id = leer_entero("ID a actualizar: ")
                servicio.buscar(id)
                nombre = input("Nuevo nombre: ")
                precio = leer_decimal("Nuevo precio: ")
                stock = leer_entero("Nuevo stock: ")
                servicio.actualizar(id, nombre, precio, stock)
                print("Videojuego actualizado correctamente.")

            elif opcion == 5:
                id = leer_entero("ID a eliminar: ")
                servicio.eliminar(id)
                print("Videojuego eliminado correctamente.")

            elif opcion == 6:
                id = leer_entero("ID del videojuego: ")
                cantidad = leer_entero("Cantidad a vender: ")
                servicio.vender(id, cantidad)
                print("Venta realizada correctamente.")

            elif opcion == 7:
                print("Saliendo del programa...")

            else:
                print("Opción no válida.")

        except ValueError as error:
            print("Error:", error)


main()