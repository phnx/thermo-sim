from thermo_sim.calculation_manager import compressor, chamber1, condenser, chamber2, expansion, chamber3, evaporator, chamber4
# a,b,c,d = compressor(226000,206843,1000000,1500)
# print(a,b,c,d)

# h1, p1 = chamber1(3,370000,1000000,0.0132623,0.0120,375696)
# print(h1, p1)

# mcondin, mcondout, hcondout, twout, mwout = condenser(370040,1000869,965000,303,22)
# print(mcondin, mcondout, hcondout, twout, mwout) 

# h2, p2 = chamber2(3,330000,965000,0.01226724,0.0120,313693)
# print(h2, p2)

# mexpain, mexpaout, hexpaout = expansion(329892,964278,220632)
# print(mexpain, mexpaout, hexpaout)

# h3, p3 = chamber3(3,240000,220632,0.011988,0.0120,329892)
# print(h3, p3)

# mevapin, mevapout, hevapout = evaporator(240789,223181,206843, 300)
# print(mevapin, mevapout, hevapout)

h4, p4 = chamber4(3,226000,206843,0.01421143,0.01326226,261894)
print(h4, p4)