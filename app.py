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
    nombre_cliente          = request.form.get("nombre-cliente")
    apellidos_cliente       = request.form.get("apellidos-cliente")

    print(nombre, apellidos)

    return redirect ("http://localhost/solicita_pedido.html", code=302)


nombre_pedidos = [
   {'nombre' : "Pedro", 'apellidos' : "Martín"}
]


nombre_cliente= [dictionary["nombre"] for dictionary in nombre_pedidos]
apellidos_cliente= [dictionary["apellidos"] for dictionary in nombre_pedidos]

for i, nombre in enumerate(nombre_cliente):
    n = nombre[i]
    for j, apellidos in enumerate (apellidos_cliente):
        a = apellidos[j]
        if i == j:
            persistencia.guardar_pedido(n, a)
