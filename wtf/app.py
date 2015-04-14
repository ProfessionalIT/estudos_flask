from flask import Flask
from flask import redirect, abort

app = Flask('wtf')


@app.route("/<name>")
def index(name):
    if name.lower() == 'leandro':
        return "Ola {}".format(name), 200
    else:
        return "Not Found", 400


@app.route("/")
def hello_world():
    return "Hello World ! <strong>I am learning Flask</strong>", 200


app.run(debug=True, use_reloader=True, port=4000)
