"""Module app"""
with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()


from flask import Flask, render_template, request, redirect, Response
import persistencia

app = Flask(__name__)

@app.route("/")
def template():
    """Prepara el pedido plantilla"""
    return render_template("prepara_pedido.html")

@app.route("/pizza", methods=['POST'])
def pizza():
    """Module route POST"""
    nombre          = request.form.get("nombre")
    apellidos       = request.form.get("apellidos")

    print(nombre, apellidos)

    return redirect ("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """Comprueba disponibilidad de un tamaño de pizza"""
    size = request.form.get("size")
    if size == "S":
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

nombre_pedidos = [
   {'nombre' : "Pedro", 'apellidos' : "Martín"}
]

nombre_cliente= [dictionary["nombre"] for dictionary in nombre_pedidos]
apellidos_cliente= [dictionary["apellidos"] for dictionary in nombre_pedidos]

for i, nombre_cliente in enumerate(nombre_cliente):
    n = nombre_cliente
    for j, apellidos_cliente in enumerate (apellidos_cliente):
        a = apellidos_cliente
        if i == j:
            persistencia.guardar_pedido(n, a)
