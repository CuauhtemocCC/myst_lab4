# python script with the main functionality
import visualizations as vs
import pandas as pd
import functions as fn
import data as dt

# Consumir datos de CCXT y visualización de microestructura.

# Microestructura
me = fn.microestructura(dt.inst,50,3600,dt.exc,dt.exchl)

# Close prices 
CPs = fn.close_prices(dt.inst,90,dt.exc)

# Modelado de Microestructura
# vs.grafos(me,dt.exchl)

# Tablas Spreads
ppp = fn.spread_cut(me,CPs,dt.exchl,dt.inst)

# Calculo de Effective Spread
es = fn.EffectiveSpread(me)

# Resultados finales
FTable = fn.ESR(ppp, es)
Resultados = fn.Salidas(FTable)

