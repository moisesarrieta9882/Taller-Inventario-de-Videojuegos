from modelo import Producto


class ProductoDAO:
    def __init__(self, base_datos):
        self.base_datos = base_datos

    def insertar(self, producto):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (producto.nombre, producto.precio, producto.stock)
        )
        conexion.commit()
        conexion.close()

    def listar(self):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos")
        filas = cursor.fetchall()
        conexion.close()

        productos = []
        for fila in filas:
            productos.append(Producto(fila[0], fila[1], fila[2], fila[3]))
        return productos

    def buscar_por_id(self, id):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
            (id,)
        )
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
            return None
        return Producto(fila[0], fila[1], fila[2], fila[3])

    def actualizar(self, producto):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
            (producto.nombre, producto.precio, producto.stock, producto.id)
        )
        conexion.commit()
        conexion.close()

    def actualizar_stock(self, id, nuevo_stock):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET stock = ? WHERE id = ?",
            (nuevo_stock, id)
        )
        conexion.commit()
        conexion.close()

    def eliminar(self, id):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()