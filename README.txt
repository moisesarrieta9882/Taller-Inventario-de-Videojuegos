Sistema de Inventario de Videojuegos

Propósito
Aplicación de consola en Python que administra el inventario de una tienda de videojuegos. Permite registrar, consultar, actualizar, eliminar y vender videojuegos, guardando todo en SQLite con el patrón DAO.

Estructura
-`modelo.py`: clase `Producto`.
-`base_datos.py`: conexión y creación de la base de datos SQLite.
-`producto_dao.py`: consultas SQL del CRUD.
-`producto_servicio.py`: validaciones y reglas del negocio.
-`main.py`: menú interactivo de consola.

Funciones
1. Registrar videojuego
2. Mostrar inventario
3. Buscar videojuego por ID
4. Actualizar videojuego
5. Eliminar videojuego
6. Vender unidades
7. Salir

Validaciones: nombre no vacío, precio mayor a 0, stock no negativo, venta mayor a 0 y sin superar el stock, ID inexistente y entradas incorrectas controladas.

Cómo ejecutar
Requiere Python 3 (SQLite ya viene incluido).

python main.py


Evidencias de pruebas
| Prueba | Resultado |

Registrar Resident Evil 4 (180000, stock 10) | Guardado correctamente 
Mostrar inventario | Aparecen los productos 
Buscar ID existente | Muestra los datos 
Actualizar producto | Cambios guardados 
Vender 3 unidades de Resident Evil 4 | Stock de 10 a 7 
Vender 20 unidades | Rechazado, stock se conserva 
Buscar ID inexistente | Informa que no existe 
Eliminar producto | Ya no aparece en el inventario 