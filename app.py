from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})
