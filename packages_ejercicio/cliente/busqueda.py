from cliente.datos import base_datos

def buscar_cliente(nombre):
    for cliente in base_datos["clientes"]:
        if cliente["Nombre"] == nombre:
            return cliente["Nombre"]
    return None