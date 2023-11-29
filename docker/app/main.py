import flask
import requests
from flask import Flask, redirect, url_for, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

aliados_api_url = "http://192.168.1.185:3002"
productos_api_url = "http://192.168.1.185:3001"


@app.route("/api/v1/eb/hello", methods=["GET"])
def api_all():
    return jsonify("Hello putos")


@app.route("/api/v1/eb/aliados", methods=["GET"])
def api_aliados():
    return requests.get(aliados_api_url + "/api/v1/aliados").json()


app.run(host="0.0.0.0", port=3000)
