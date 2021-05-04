"""
Thermo-Sim POC
last update 20210504
"""
import json
import os

from flask import Flask, request, render_template

from thermo_sim import calculate_1, calculate_2, calculate_3, compressor, chamber1, condenser, chamber2, expansion, chamber3, evaporator, chamber4

app = Flask(__name__)

@app.route("/calculate", methods=["GET"])
def calculation() -> str:
    calculation_1_result = None
    calculation_2_result = None
    calculation_3_result = None
    compressor = None
    chamber1 = None
    condenser = None
    chamber2 = None
    expansion = None
    chamber3 = None
    evaporator = None
    chamber4 = None

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

@app.route("/refrigeration", methods=["GET"])
def refrigeration() -> str:
    if (request.args.get("h1") is None
        or request.args.get("h2") is None
        or request.args.get("h3") is None
        or request.args.get("h4") is None
        or request.args.get("p1") is None
        or request.args.get("p2") is None
        or request.args.get("p3") is None
        or request.args.get("p4") is None
        or request.args.get("mcompin") is None
        or request.args.get("mcompout") is None
        or request.args.get("mcondin") is None
        or request.args.get("mcondout") is None
        or request.args.get("mexpain") is None
        or request.args.get("mexpaout") is None
        or request.args.get("mevapin") is None
        or request.args.get("mevapout") is None
        
        or request.args.get("hcompout") is None
        or request.args.get("hcondout") is None
        or request.args.get("hexpaout") is None
        or request.args.get("hevapout") is None

        or request.args.get("pump_rpm") is None
        or request.args.get("twin") is None
        or request.args.get("wvalve") is None
        or request.args.get("heater") is None
        or request.args.get("dt") is None):

        h1 = 370000
        h2 = 330000
        h3 = 240000
        h4 = 226000
        p1 = 1000000
        p2 = 965000
        p3 = 220632
        p4 = 206843

        mcompin = 0.012
        mcompout = 0.011
        mcondin = 0.012
        mcondout = 0.011
        mexpain = 0.012
        mexpaout = 0.011
        mevapin = 0.012
        mevapout = 0.011
        hcompout = 380000
        hcondout = 230000
        hexpaout = 230000
        hevapout = 360000

        pump_rpm = 1500
        twin = 303
        wvalve = 22
        heater = 300
        dt = 3

        weight_scale = 1
        twout = 1
        mwout = 1

    else:
        h1 = float(request.args.get("h1"))
        h2 = float(request.args.get("h2"))
        h3 = float(request.args.get("h3"))
        h4 = float(request.args.get("h4"))
        p1 = float(request.args.get("p1"))
        p2 = float(request.args.get("p2"))
        p3 = float(request.args.get("p3"))
        p4 = float(request.args.get("p4"))

        mcompin = float(request.args.get("mcompin"))
        mcompout = float(request.args.get("mcompout"))
        mcondin = float(request.args.get("mcondin"))
        mcondout = float(request.args.get("mcondout"))
        mexpain = float(request.args.get("mexpain"))
        mexpaout = float(request.args.get("mexpaout"))
        mevapin = float(request.args.get("mevapin"))
        mevapout = float(request.args.get("mevapout"))
        hcompout = float(request.args.get("hcompout"))
        hcondout = float(request.args.get("hcondout"))
        hexpaout = float(request.args.get("hexpaout"))
        hevapout = float(request.args.get("hevapout"))

        pump_rpm = float(request.args.get("pump_rpm"))
        twin = float(request.args.get("twin"))
        wvalve = float(request.args.get("wvalve"))
        heater = float(request.args.get("heater"))
        dt = float(request.args.get("dt"))

    if request.args.get("pump_rpm") is not None and request.args.get("twin") is not None and request.args.get("wvalve") is not None and request.args.get("heater") is not None and request.args.get("dt") is not None:
        compressor_result = compressor(h4, p4, p1, pump_rpm)
        chamber1_result = chamber1(dt, h1, p1, mcompout, mcondin, hcompout)
        condenser_result = condenser(h1, p1, p2, twin, wvalve)
        chamber2_result = chamber2(dt, h2, p2, mcondout, mexpain, hcondout)
        expansion_result = expansion(h2, p2, p3)
        chamber3_result = chamber3(dt, h3, p3, mexpaout, mevapin, hexpaout)
        evaporator_result = evaporator(h3, p3, p4, heater)
        chamber4_result = chamber4(dt, h4, p4, mevapout, mcompin, hevapout)
        
        # h1 = compressor_result[0]

    return response_formatter({

        "h1": chamber1_result[0],
        "p1": chamber1_result[1],
        "h2": chamber2_result[0],
        "p2": chamber2_result[1],
        "h3": chamber3_result[0],
        "p3": chamber3_result[1],
        "h4": chamber4_result[0],
        "p4": chamber4_result[1],     

        "mcompin": compressor_result[0],
        "mcompout": compressor_result[1],
        "hcompout": compressor_result[2],
        "weight_scale": compressor_result[3],
        "mcondin": condenser_result[0],
        "mcondout": condenser_result[1],
        "hcondout": condenser_result[2],
        "twout": condenser_result[3],
        "mwout": condenser_result[4],
        "mexpain": expansion_result[0],
        "mexpaout": expansion_result[1],
        "hexpaout": expansion_result[2],
        "mevapin": evaporator_result[0],
        "mevapout": evaporator_result[1],
        "hevapout": evaporator_result[2],

        "pump_rpm": pump_rpm,
        "twin": twin,
        "wvalve": wvalve
        }
    )

@app.route("/")
def main():
    return render_template('main.html')


# ================================

def response_formatter(data: dict) -> str:
    return json.dumps(data)