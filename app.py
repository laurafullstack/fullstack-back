with open("pedidos.txt", "w", encoding="utf-8") as file:
 file.write("")
 file.close()


from flask import Flask, render_template, request, redirect
import pedidos

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("prepara_pedido.html")

@app.route("/pizza", methods=['POST'])
def pizza():
    nombre          = request.form.get("nombre-cliente")
    apellidos       = request.form.get("apellidos-cliente")

    print(nombre, apellidos)

    return redirect ("http://localhost/solicita_pedido.html", code=302)


nombre_pedidos = [
   {'nombre' : "Pedro", 'apellidos' : "Martín"}
]


nombre= [dictionary["nombre"] for dictionary in nombre_pedidos]
apellidos= [dictionary["apellidos"] for dictionary in nombre_pedidos]

for i in range(len(nombre)):
    n = nombre[i]
    for j in range(len(apellidos)):
       a = apellidos[j]
       if(i == j):
            pedidos.guardar_pedido(n, a)