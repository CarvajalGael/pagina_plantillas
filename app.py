from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/autos")
def autos():
    return render_template("autos.html")

@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")

@app.route("/acercas")
def acercas():
    return render_template("acercas.html")

if __name__ == '__main__':
    app.run(debug=True)




