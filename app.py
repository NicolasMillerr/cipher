from flask import Flask, request
from flask_restx import Api, Resource
from cipher.caesar import Caesar

app = Flask(__name__)
api = Api(app)


@api.route("/encode")
class Encode(Resource):
    def post(self):
        key = int(request.form["key"])
        plaintext = request.form["plaintext"]
        machine = Caesar(key)
        ciphertext = machine.encode(plaintext)
        return {"ciphertext": ciphertext}


@api.route("/decode")
class Decode(Resource):
    def post(self):
        key = int(request.form["key"])
        ciphertext = request.form["ciphertext"]
        machine = Caesar(key)
        plaintext = machine.decode(ciphertext)
        return {"plaintext": plaintext}


if __name__ == "__main__":
    app.run(debug=True)
