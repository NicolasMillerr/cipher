from flask import Flask, request
from flask_restx import Api, Resource
from cipher import encode, decode

app = Flask(__name__)
api = Api(app)


@api.route("/encode")
class Encode(Resource):
    def post(self):
        ciphertext = encode(request.form["plaintext"], int(request.form["order"]))
        return {"ciphertext": ciphertext}


@api.route("/decode")
class Decode(Resource):
    def post(self):
        plaintext = decode(request.form["ciphertext"], int(request.form["order"]))
        return {"plaintext": plaintext}


if __name__ == "__main__":
    app.run(debug=True)