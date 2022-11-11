# python script with the main functionality
import visualizations as vs
import functions as fn
import data as dt

# Consumir datos de CCXT y visualización de microestructura.

# Microestructura
me = fn.microestructura(dt.inst,50,120,dt.exc,dt.exchl)

# Close prices 
CPs = fn.close_prices(dt.inst,30,dt.exc)

# Modelado de Microestructura
vs.grafos(dt.me,dt.exchl)

# Tablas Spreads
ppp = fn.spread_cut(me,CPs,dt.exchl,dt.inst)

# Calculo de Effective Spread
es = fn.EffectiveSpread(me)

Salidas = fn.ESR(ppp, es)

Salida_B1 = Salidas[0]
Salida_B2 = Salidas[1]
Salida_B3 = Salidas[2]
Salida_G1 = Salidas[3]
Salida_G2 = Salidas[4]
Salida_G3 = Salidas[5]
Salida_O1 = Salidas[6]
Salida_O2 = Salidas[7]
Salida_O3 = Salidas[8]