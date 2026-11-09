from modelo import Producto


class ProductoServicio:
    def __init__(self, dao):
        self.dao = dao

    def validar_datos(self, nombre, precio, stock):
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

    def registrar(self, nombre, precio, stock):
        self.validar_datos(nombre, precio, stock)
        producto = Producto(None, nombre.strip(), precio, stock)
        self.dao.insertar(producto)

    def listar(self):
        return self.dao.listar()

    def buscar(self, id):
        producto = self.dao.buscar_por_id(id)
        if producto is None:
            raise ValueError(f"No existe un videojuego con el ID {id}.")
        return producto

    def actualizar(self, id, nombre, precio, stock):
        self.buscar(id)
        self.validar_datos(nombre, precio, stock)
        producto = Producto(id, nombre.strip(), precio, stock)
        self.dao.actualizar(producto)

    def eliminar(self, id):
        self.buscar(id)
        self.dao.eliminar(id)

    def vender(self, id, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        producto = self.buscar(id)
        if cantidad > producto.stock:
            raise ValueError(
                f"No hay suficiente stock. Disponible: {producto.stock}."
            )
        nuevo_stock = producto.stock - cantidad
        self.dao.actualizar_stock(id, nuevo_stock)