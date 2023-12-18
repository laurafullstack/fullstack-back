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
    nombre          = request.form.get("nombre-cliente")
    apellidos       = request.form.get("apellidos-cliente")

    print(nombre, apellidos)

    return redirect ("http://localhost/solicita_pedido.html", code=302)


nombre_pedidos = [
   {'nombre' : "Pedro", 'apellidos' : "Martín"}
]


nombre= [dictionary["nombre-cliente"] for dictionary in nombre_pedidos]
apellidos= [dictionary["apellidos-cliente"] for dictionary in nombre_pedidos]

for i in range(len(nombre)):
    n = nombre[i]
    for j in range(len(apellidos)):
        a = apellidos[j]
        if i == j:
            persistencia.guardar_pedido(n, a)
