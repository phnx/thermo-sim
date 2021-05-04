# from os import environ

import CoolProp.CoolProp as CP
# from CoolProp.CoolProp import PhaseSI, PropsSI, get_global_param_string

# def retrieving_constant():
    # CONSTANT = environ.get('CONSTANT')

def calculate_1(var_1: float, var_2: float) -> float:
    # CP can be used here with 2 input variables
    aa = 20.0
    aa = var_1/100*(100-aa) + aa
    bb = CP.PropsSI("T", "P", var_1, "Q", 0, "Water")
    aa = aa + bb + 1
    return bb

def compressor(h4: float, p4: float, p1: float, pump_rpm: float) -> [float, float, float, float]:
    hcompin = h4
    pcompin = p4
    pcompout = p1
    
    bore = 0.0413
    stroke = 0.038
    volume_eff = 0.85
    mech_eff = 0.35
    motor_arm = 0.3

    swept_volume = 3.14*bore*bore/4*stroke*pump_rpm/60 
    accual_volume = swept_volume*volume_eff

    if CP.PropsSI("H","Q",1,"P",pcompin,"R12") > hcompin:
        hcompin = CP.PropsSI("H","Q",1,"P",pcompin,"R12")

    density = CP.PropsSI("D","H",hcompin,"P",pcompin,"R12")
    scompin = CP.PropsSI("S","H",hcompin,"P",pcompin,"R12")
    mcompin = accual_volume*density
    mcompout = mcompin
    scompout = scompin

    hcompout = CP.PropsSI("H","S",scompout,"P",pcompout,"R12")
    weight_scale = mcompin*(hcompout-hcompin)/(mech_eff*9.81*motor_arm*pump_rpm*2*3.14/60)
    
    return mcompin, mcompout, hcompout, weight_scale

def chamber1(dt: float, h1: float, p1: float, mcompout: float, mcondin: float, hcompout: float) -> [float, float]:
    volume1 = 0.1

    h1_1 = h1
    p1_1 = p1
    m1in = mcompout
    m1out = mcondin
    h1in = hcompout

    density = CP.PropsSI("D","H",h1_1,"P",p1_1,"R12")
    m1_1 = density*volume1
    m1 = m1_1+(m1in-m1out)*dt
    density = m1/volume1

    h1 = ((m1_1*h1_1)+(m1in*h1in-m1out*h1_1)*dt)/m1_1
    p1 = CP.PropsSI("P","H",h1,"D",density,"R12")

    return h1, p1

def condenser(h1: float, p1: float, p2: float, twin: float, wvalve: float) -> [float, float, float, float, float]:
    hcondin = h1
    pcondin = p1
    pcondout = p2
    mwin = 0.203*wvalve/100
    mwout = mwin

    epsilon = 0.15
    cpw = 4120
    cpr12 = 728
    kcond = 3.42*(10.0**(-7.0))

    latentr12 = CP.PropsSI("H","P",pcondin,"Q",1,"R12") - CP.PropsSI("H","P",pcondin,"Q",0,"R12")
    mcondin = kcond*(pcondin - pcondout)
    mcondout = mcondin
    ch = mcondin*( cpr12 + latentr12/CP.PropsSI("T","P",pcondin,"Q",1,"R12") )
    cc = cpw*mwin*2
    cmin = cc
    qmax = cmin*( CP.PropsSI("T","H",hcondin,"P",pcondin,"R12") - twin)
    qacc = epsilon*qmax
    twout = twin+qacc/mwin/cpw
    hcondout = (mcondin*hcondin - qacc)/mcondout

    return mcondin, mcondout, hcondout, twout, mwout

def chamber2(dt: float, h2: float, p2: float, mcondout: float, mexpain: float, hcondout: float) -> [float, float]:
    volume2 = 0.1

    h2_1 = h2
    p2_1 = p2
    m2in = mcondout
    m2out = mexpain
    h2in = hcondout

    density = CP.PropsSI("D","H",h2_1,"P",p2_1,"R12")
    m2_1 = density*volume2
    m2 = m2_1+(m2in-m2out)*dt
    density = m2/volume2

    h2 = ((m2_1*h2_1)+(m2in*h2in-m2out*h2_1)*dt)/m2_1
    p2 = CP.PropsSI("P","H",h2,"D",density,"R12")

    return h2, p2

def expansion(h2: float, p2: float, p3: float) -> [float, float, float]:
    hexpain = h2
    pexpain = p2
    pexpaout = p3
    kexpa = 1.612*(10**(-8))

    mexpain = kexpa*(pexpain - pexpaout)
    mexpaout = mexpain
    hexpaout = hexpain

    return mexpain, mexpaout, hexpaout

def chamber3(dt: float, h3: float, p3: float, mexpaout: float, mevapin: float, hexpaout: float) -> [float, float]:
    volume3 = 0.1

    h3_1 = h3
    p3_1 = p3
    m3in = mexpaout
    m3out = mevapin
    h3in = hexpaout

    density = CP.PropsSI("D","H",h3_1,"P",p3_1,"R12")
    m3_1 = density*volume3
    m3 = m3_1+(m3in-m3out)*dt
    density = m3/volume3

    h3 = ((m3_1*h3_1)+(m3in*h3in-m3out*h3_1)*dt)/m3_1
    p3 = CP.PropsSI("P","H",h3,"D",density,"R12")

    return h3, p3

def evaporator(h3: float, p3: float, p4: float, heater: float) -> [float, float, float]:

    hevapin = h3
    pevapin = p3
    pevapout = p4

    kevap = 8.7*(10**(-7))

    mevapin = kevap*(pevapin - pevapout)
    mevapout = mevapin
    hevapout = hevapin + heater/mevapout

    return mevapin, mevapout, hevapout

def chamber4(dt: float, h4: float, p4: float, mevapout: float, mcompin: float, hevapout: float) -> [float, float]:
    volume4 = 0.1

    h4_1 = h4
    p4_1 = p4
    m4in = mevapout
    m4out = mcompin
    h4in = hevapout

    density = CP.PropsSI("D","H",h4_1,"P",p4_1,"R12")
    m4_1 = density*volume4
    m4 = m4_1+(m4in-m4out)*dt
    density = m4/volume4

    h4 = ((m4_1*h4_1)+(m4in*h4in-m4out*h4_1)*dt)/m4_1
    p4 = CP.PropsSI("P","H",h4,"D",density,"R12")

    return h4, p4

def calculate_2(var_1: float, var_2: float) -> float:
    # CP can be used here with 2 input variables
    return var_1 * var_2

def calculate_3(var_1: float, var_2: float) -> float:
    # CP can be used here with 2 input variables
    return var_1 - var_2