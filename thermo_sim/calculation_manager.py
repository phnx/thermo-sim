# from os import environ

import CoolProp.CoolProp as CP
# from CoolProp.CoolProp import PhaseSI, PropsSI, get_global_param_string

# def retrieving_constant():
    # CONSTANT = environ.get('CONSTANT')

def calculate_1(var_1: float, var_2: float) -> float:
    # CP can be used here with 2 input variables
    a = var_1/100*(100-a) + a
    b = CP.PropsSI("T", "P", var_1, "Q", 0, "Water")
    a = a + b + 1
    return b

def calculate_2(var_1: float, var_2: float) -> float:
    # CP can be used here with 2 input variables
    return var_1 * var_2

def calculate_3(var_1: float, var_2: float) -> float:
    # CP can be used here with 2 input variables
    return var_1 - var_2