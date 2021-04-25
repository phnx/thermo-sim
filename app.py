"""
Thermo-Sim POC
"""
import json
import os

from flask import Flask, request, render_template

from thermo_sim import calculate

app = Flask(__name__)

@app.route("/calculate", methods=["GET"])
def calculation() -> str:
    screen_result = None

    if request.args.get("var_1") is not None and request.args.get("var_2") is not None:
        calculation_result  = calculate(
            var_1=float(request.args.get("var_1")),
            var_2=float(request.args.get("var_2"))
        )

    return response_formatter({"calculation_result": calculation_result})

@app.route("/")
def main():
    return render_template('main.html')


# ================================

def response_formatter(data: dict) -> str:
    return json.dumps(data)