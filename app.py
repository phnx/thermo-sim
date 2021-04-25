"""
Thermo-Sim POC
"""
import json
import os

from flask import Flask, request, render_template

from thermo_sim import calculate_1, calculate_2, calculate_3

app = Flask(__name__)

@app.route("/calculate", methods=["GET"])
def calculation() -> str:
    calculation_1_result = None
    calculation_2_result = None
    calculation_3_result = None

    if request.args.get("var_1") is not None and request.args.get("var_2") is not None:
        calculation_1_result  = calculate_1(
            var_1=float(request.args.get("var_1")),
            var_2=float(request.args.get("var_2"))
        )
        calculation_2_result  = calculate_2(
            var_1=float(request.args.get("var_1")),
            var_2=float(request.args.get("var_2"))
        )
        calculation_3_result  = calculate_3(
            var_1=float(request.args.get("var_1")),
            var_2=float(request.args.get("var_2"))
        )

    return response_formatter({
        "calculation_1_result": calculation_1_result,
        "calculation_2_result": calculation_2_result,
        "calculation_3_result": calculation_3_result
        }
    )

@app.route("/")
def main():
    return render_template('main.html')


# ================================

def response_formatter(data: dict) -> str:
    return json.dumps(data)