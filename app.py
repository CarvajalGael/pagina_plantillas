from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_y_dificil_de_adivinar'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/autos")
def autos():
    return render_template("autos.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")



@app.route("/registrame", methods=["GET", "POST"])
def registrame():
    if request.method == "POST":
        nombreCompleto = request.form["nombreCompleto"]
        email = request.form["email"]
        password = request.form["password"]
        confirmPassword = request.form["confirmPassword"]
        
        error = None
        if not nombreCompleto or not email or not password or not confirmPassword:
            error = "Todos los campos son obligatorios"
        
        if password != confirmPassword:
            error = "La contraseña no coincide"
        
        if error:
            flash(error, 'error')
            return render_template("registro.html")
        else:
            flash(f"¡Registro exitoso para el usuario: {nombreCompleto}!", 'success')
            return redirect(url_for('index'))

    return render_template("registro.html")


def validaLogin():
    password = request.form.get('password')

    if not email or not password:
        flash("pr favor de ingresar email y contraseña", "error")
    elif email not in USUARIOS_REGISTRADOS:
        flash("Correo no registrado", "error")
    elif USUARIOS_REGISTRADOS[email]['password'] != password:
        flash("Contraseña incorrecta", "error")
    else:
        session['usuario_email'] = email
        session['usuario_nombre'] = USUARIOS_REGISTRADOS[email]['nombre']
        session['logeando'] = True

        flash("Inicio de sesión exitoso", "success")
        return redirect(url_for('bienvenido'))


@app.route("/acercas")
def acercas():
    return render_template("acercas.html")

if __name__ == '__main__':
    app.run(debug=True)
                                                