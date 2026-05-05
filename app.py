from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev"

@app.route("/", methods=["GET"])
def raiz():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # validação fake só para navegar
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", tot_alunos=2, tot_matriculas=1, tot_pendencias=1)

@app.route("/cadastro-aluno", methods=["GET","POST"])
def cadastro_aluno():
    if request.method == "POST":
        # aqui você trataria e salvaria no BD
        return redirect(url_for("dashboard"))
    return render_template("cadastro_aluno.html")

@app.route("/matricula", methods=["GET","POST"])
def matricula():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("matricula.html")

@app.route("/documentos", methods=["GET","POST"])
def documentos():
    if request.method == "POST":
        return redirect(url_for("relatorios"))
    return render_template("documentos.html")

@app.route("/relatorios", methods=["GET"])
def relatorios():
    return render_template("relatorio.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001) 

