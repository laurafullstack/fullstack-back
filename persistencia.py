"""Module persistencia"""
def guardar_pedido(nombre, apellidos):
    """Module persistencia función"""
    with open("pedidos.txt", "a",encoding="UTF-8")as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
