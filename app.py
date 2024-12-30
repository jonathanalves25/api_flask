from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Página Home"


@app.route("/about")
def about():
    return "Essa é a pagina sobre"


app.run(debug=True)
