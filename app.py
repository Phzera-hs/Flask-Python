from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/times")
def times():
    return render_template("sobre.html")  

@app.route("/jogadores")
def jogadores():
    return render_template("jogador.html") 

if __name__ == "__main__":
   app.run(debug=True, port=5000)  