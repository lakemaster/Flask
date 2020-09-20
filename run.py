# coding=utf-8
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name")
    items = ["Apfel", "Birne", "Traube"]
    return render_template("start.html", name=name, items=items)


@app.route("/test")
def funktionXYZ():
    name = request.args.get("name")
    return render_template("test.html", name=name)


def calc_value_map(self, fx_rate):
    value_map = {}
    if fx_rate != None:
        for i in [1, 10, 1000, 1000000]:
            value_map[i] = i * fx_rate
    return value_map

@app.route("/currencies")
def getCurrenciesPage():
    ccy_map = {"USD":1.07306, "SEK":11.1082, "NOK":12.4283, "GBP":0.92572}
    ccy = request.args.get("ccy")
    value_map = calc_value_map(ccy, ccy_map.get(ccy))
    return render_template("currencies.html", ccy=ccy, ccy_map=ccy_map, value_map=value_map)

