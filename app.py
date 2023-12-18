"""Module app"""
with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()


from flask import Flask, render_template, request, redirect
import persistencia

app = Flask(__name__)

@app.route("/")
def template():
    """Module app route"""
    return render_template("prepara_pedido.html")

@app.route("/pizza", methods=['POST'])
def pizza():
    """Module route POST"""
    nombre          = request.form.get("nombre")
    apellidos       = request.form.get("apellidos")

    print(nombre, apellidos)

    return redirect ("http://localhost/solicita_pedido.html", code=302)


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
