# Makeup Inventory Project

Sistema de gestión de inventario para productos de maquillaje desarrollado en Python, utilizando programación orientada a objetos (POO) y manejo de archivos. La aplicación funciona a través de consola y permite realizar operaciones básicas de una bodega.

---
## Tecnologías utilizadas

- Python 
- Manejo de clases y objetos
- Archivos JSON para almacenamiento
- Consola interactiva

---

## Funcionalidades principales

Este sistema incluye las siguientes opciones de menú:

1. **Mostrar inventario**  
   Lista todos los productos actualmente almacenados.

2. **Registrar entrada de stock**  
   Permite ingresar nuevas unidades de un producto existente o nuevo.

3. **Registrar salida de stock**  
   Registra la salida de unidades de un producto (por venta, uso, etc).

4. **Buscar producto por ID**  
   Permite buscar información de un producto mediante su identificador.

5. **Mostrar historial de movimientos**  
   Muestra las entradas y salidas registradas por producto.

6. **Revisar productos vencidos**  
   Revisa y lista los productos cuya fecha de expiración ha pasado.

7. **Guardar inventario en JSON**  
   Guarda el estado actual del inventario en un archivo `.json`.

8. **Agregar producto manualmente**  
   Añade un nuevo producto ingresando sus datos manualmente.

9. **Eliminar producto por ID**  
   Elimina un producto específico del inventario.

0. **Salir**  
   Finaliza el programa.

# Diagrama de Clases

# Diagrama de Clases

```mermaid
classDiagram

class Product {
    - name: str
    - id: int
    - price: float
    - brand: str
    + __str__(): str
}

class Makeup {
    - color: str
    - size: float
    - expiration_date: date
    - expired: bool
    + __str__(): str
}

class Perfume {
    - scent: str
    - volume: float
    + __str__(): str
}

class MovementRecord {
    - product_id: int
    - type: str
    - quantity: int
    - date: datetime
    + __str__(): str
}

class Stock {
    - products: dict
    - inventory: dict
    - history: list
    + add_product(product)
    + register_entry(product_id, amount)
    + register_output(product_id, amount)
    + show_inventory()
    + show_history()
    + find_product(product_id)
    + check_expirations()
}

Product <|-- Makeup
Product <|-- Perfume
Stock --> Product : manages
Stock --> MovementRecord : logs

```

