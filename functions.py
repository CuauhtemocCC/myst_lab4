# python script with general functions     


import pandas as pd
import numpy as np
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def OB(inst:str,limit:int,t:int,exchange:str):
    tiempo = round(time.time())
    time_f = 0
    tl = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    l9 = []
    while time_f <= t:
        extr = exchange[0].fetch_order_book(inst[0],limit=limit)
        extr2 = exchange[0].fetch_order_book(inst[1],limit=limit)
        extr3 = exchange[0].fetch_order_book(inst[2],limit=limit)
        extr4 = exchange[1].fetch_order_book(inst[0],limit=limit)
        extr5 = exchange[1].fetch_order_book(inst[1],limit=limit)
        extr6 = exchange[1].fetch_order_book(inst[2],limit=limit)
        extr7 = exchange[2].fetch_order_book(inst[0],limit=limit)
        extr8 = exchange[2].fetch_order_book(inst[1],limit=limit)
        extr9 = exchange[2].fetch_order_book(inst[2],limit=limit)
        l1.append(extr)
        l2.append(extr2)
        l3.append(extr3)
        l4.append(extr4)
        l5.append(extr5)
        l6.append(extr6)        
        l7.append(extr7)
        l8.append(extr8)
        l9.append(extr9)        
        time_f = round(time.time()) - tiempo
    tl.append(l1)
    tl.append(l2)
    tl.append(l3)
    tl.append(l4)
    tl.append(l5)
    tl.append(l6)    
    tl.append(l7)
    tl.append(l8)
    tl.append(l9)    
    return tl

def close_prices(inst,limite,exc):
    o1 = exc[0].fetch_ohlcv(inst[0], '1m', limit=limite)
    t1 = pd.DataFrame(o1).drop([1,2,3,5],axis=1)
    t1.columns = ['milliseconds', 'CP'+' '+str(inst[0])+' '+str(exc[0])]
    o2 = exc[0].fetch_ohlcv(inst[1], '1m', limit=limite)
    t2 = pd.DataFrame(o2).drop([0,1,2,3,5],axis=1)
    t2.columns = ['CP'+' '+str(inst[1])+' '+str(exc[0])]
    o3 = exc[0].fetch_ohlcv(inst[2], '1m', limit=limite)
    t3 = pd.DataFrame(o3).drop([0,1,2,3,5],axis=1)
    t3.columns = ['CP'+' '+str(inst[2])+' '+str(exc[0])]

    o4 = exc[1].fetch_ohlcv(inst[0], '1m', limit=limite)
    t4 = pd.DataFrame(o4).drop([0,1,2,3,5],axis=1)
    t4.columns = ['CP'+' '+str(inst[0])+' '+str(exc[1])]
    o5 = exc[1].fetch_ohlcv(inst[1], '1m', limit=limite)
    t5 = pd.DataFrame(o5).drop([0,1,2,3,5],axis=1)
    t5.columns = ['CP'+' '+str(inst[1])+' '+str(exc[1])]
    o6 = exc[1].fetch_ohlcv(inst[2], '1m', limit=limite)
    t6 = pd.DataFrame(o6).drop([0,1,2,3,5],axis=1)
    t6.columns = ['CP'+' '+str(inst[2])+' '+str(exc[1])]

    o7 = exc[2].fetch_ohlcv(inst[0], '1m', limit=limite)
    t7 = pd.DataFrame(o7).drop([0,1,2,3,5],axis=1)
    t7.columns = ['CP'+' '+str(inst[0])+' '+str(exc[2])]
    o8 = exc[2].fetch_ohlcv(inst[1], '1m', limit=limite)
    t8 = pd.DataFrame(o8).drop([0,1,2,3,5],axis=1)
    t8.columns = ['CP'+' '+str(inst[1])+' '+str(exc[2])]
    o9 = exc[2].fetch_ohlcv(inst[2], '1m', limit=limite)
    t9 = pd.DataFrame(o9).drop([0,1,2,3,5],axis=1)
    t9.columns = ['CP'+' '+str(inst[2])+' '+str(exc[2])]
    
    CPs = pd.concat([t1,t2,t3,t4,t5,t6,t7,t8,t9],axis=1)
    
    CPs["timestamp2"] = np.zeros(len(CPs.iloc[:,0]))
    for i in range(len(CPs.iloc[:,0])):
        CPs.iloc[i,10] = str(datetime.fromtimestamp(CPs.iloc[i,0]//1000).isoformat())

    return CPs

def microestructura(inst,limite,t,exc,exchl):
    vv = OB(inst,limite,t,exc)
    sy = []
    ss = []
    ts = []
    for j in range(len(vv)):
        for i in range(len(vv[j])):
            dt = vv[j][i]["datetime"]
            sb = vv[j][i]["symbol"]
            tss = vv[j][i]["timestamp"]
            ss.append(dt)
            sy.append(sb)
            ts.append(tss)

    long = len(ss)

    tabla = pd.DataFrame({'exchange':np.zeros(long),
                              'symbol':sy,
                             'timestamp':ss,
                              'milliseconds':ts,
                             'level':np.zeros(long),
                             'ask_volume':np.zeros(long),
                             'bid_volume':np.zeros(long),
                             'total_volume':np.zeros(long),
                             'mid_price':np.zeros(long),
                             'VWAP':np.zeros(long),'Spread':np.zeros(long),'timestamp2':np.zeros(long)})

    for i in range(long):
        if i < len(ss)/3:
            tabla.iloc[i,0] = exchl[0]
        elif i < len(ss)/3*2:
            tabla.iloc[i,0] = exchl[1]
        else:
            tabla.iloc[i,0] = exchl[2]

    pa = []
    qa = []
    pb = []
    qb = []
    for j in range(len(vv)):
        for i in range(len(vv[j])):
                bi_btc_ob_ask = pd.DataFrame(vv[j][i]['asks'], columns = ['price ask','quantity ask'])
                bi_btc_ob_bid = pd.DataFrame(vv[j][i]['bids'], columns = ['price bid','quantity bid'])
                pa_v = bi_btc_ob_ask['price ask'].to_list()
                qa_v = bi_btc_ob_ask['quantity ask'].to_list()
                pb_v = bi_btc_ob_bid['price bid'].to_list()
                qb_v = bi_btc_ob_bid['quantity bid'].to_list()
                pa.append(pa_v)
                qa.append(qa_v)
                pb.append(pb_v)
                qb.append(qb_v)

    pa_df = pd.DataFrame(pa).T
    qa_df = pd.DataFrame(qa).T
    pb_df = pd.DataFrame(pb).T
    qb_df = pd.DataFrame(qb).T

    tabla["level"] = limite
    for m in range(len(tabla['level'])):
        tabla.iloc[m,5] = qa_df.iloc[:,m].sum()
        tabla.iloc[m,6] = qb_df.iloc[:,m].sum()
        tabla.iloc[m,7] = tabla.iloc[m,5] + tabla.iloc[m,6]
        tabla.iloc[m,8] = (pa_df.iloc[0,m] + pb_df.iloc[0,m])/2
        tabla.iloc[m,9] = (pa_df.iloc[0,m]*qa_df.iloc[0,m] + pb_df.iloc[0,m]*qb_df.iloc[0,m])/(qb_df.iloc[0,m]+qa_df.iloc[0,m])
        tabla.iloc[m,10] = (pa_df.iloc[0,m] - pb_df.iloc[0,m])
        tabla.iloc[m,11] = tabla.iloc[m,2][0:19]
    
    return tabla

def spread_cut(me,CPs,exchl,inst):
    me2 = me
    for i in range(len(me2["timestamp"])):
        me2.iloc[i,11] = me2.iloc[i,2][0:16]
    
    cp1 = me2[(me2["exchange"] == exchl[0]) & (me2["symbol"] == inst[0])]
    cp1 = cp1.drop_duplicates(subset=['timestamp2'])
    cp1 = cp1.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp1 = cp1.set_index("timestamp2")
    cp2 = me2[(me2["exchange"] == exchl[0]) & (me2["symbol"] == inst[1])]
    cp2 = cp2.drop_duplicates(subset=['timestamp2'])
    cp2 = cp2.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp2 = cp2.set_index("timestamp2")
    cp3 = me2[(me2["exchange"] == exchl[0]) & (me2["symbol"] == inst[2])]
    cp3 = cp3.drop_duplicates(subset=['timestamp2'])
    cp3 = cp3.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp3 = cp3.set_index("timestamp2")
    cp4 = me2[(me2["exchange"] == exchl[1]) & (me2["symbol"] == inst[0])]
    cp4 = cp4.drop_duplicates(subset=['timestamp2'])
    cp4 = cp4.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp4 = cp4.set_index("timestamp2")
    cp5 = me2[(me2["exchange"] == exchl[1]) & (me2["symbol"] == inst[1])]
    cp5 = cp5.drop_duplicates(subset=['timestamp2'])
    cp5 = cp5.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp5 = cp5.set_index("timestamp2")
    cp6 = me2[(me2["exchange"] == exchl[1]) & (me2["symbol"] == inst[2])]
    cp6 = cp6.drop_duplicates(subset=['timestamp2'])
    cp6 = cp6.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp6 = cp6.set_index("timestamp2")
    cp7 = me2[(me2["exchange"] == exchl[2]) & (me2["symbol"] == inst[0])]
    cp7 = cp7.drop_duplicates(subset=['timestamp2'])
    cp7 = cp7.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp7 = cp7.set_index("timestamp2")
    cp8 = me2[(me2["exchange"] == exchl[2]) & (me2["symbol"] == inst[1])]
    cp8 = cp8.drop_duplicates(subset=['timestamp2'])
    cp8 = cp8.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp8 = cp8.set_index("timestamp2")
    cp9 = me2[(me2["exchange"] == exchl[2]) & (me2["symbol"] == inst[2])]
    cp9 = cp9.drop_duplicates(subset=['timestamp2'])
    cp9 = cp9.drop(['timestamp','milliseconds','level','ask_volume','bid_volume','total_volume','mid_price','VWAP'],axis=1)
    cp9 = cp9.set_index("timestamp2")
    
    CPs2 = CPs
    dif = 6*3600*1000
    
    for i in range(len(CPs2.iloc[:,0])):
        CPs2.iloc[i,0] = CPs2.iloc[i,0]+dif
        CPs2.iloc[i,10] = str(datetime.fromtimestamp(CPs2.iloc[i,0]//1000).isoformat())
        CPs2.iloc[i,10] = CPs2.iloc[i,10][0:16]

    CPs2 = CPs2.set_index("timestamp2")
    CPs2 = CPs2.drop(['milliseconds'],axis=1)
    
    cl1 = pd.DataFrame(CPs2.iloc[:,0],CPs2.index)
    cl2 = pd.DataFrame(CPs2.iloc[:,1],CPs2.index)
    cl3 = pd.DataFrame(CPs2.iloc[:,2],CPs2.index)
    cl4 = pd.DataFrame(CPs2.iloc[:,3],CPs2.index)
    cl5 = pd.DataFrame(CPs2.iloc[:,4],CPs2.index)
    cl6 = pd.DataFrame(CPs2.iloc[:,5],CPs2.index)
    cl7 = pd.DataFrame(CPs2.iloc[:,6],CPs2.index)
    cl8 = pd.DataFrame(CPs2.iloc[:,7],CPs2.index)
    cl9 = pd.DataFrame(CPs2.iloc[:,8],CPs2.index)
    
    jcp1 = cp1.join(cl1)
    jcp1 = jcp1[jcp1.Spread.notnull()]
    jcp1 = jcp1.drop(['exchange','symbol'],axis=1)
    jcp2 = cp2.join(cl2)
    jcp2 = jcp2[jcp2.Spread.notnull()]
    jcp2 = jcp2.drop(['exchange','symbol'],axis=1)
    jcp3 = cp3.join(cl3)
    jcp3 = jcp3[jcp3.Spread.notnull()]
    jcp3 = jcp3.drop(['exchange','symbol'],axis=1)
    jcp4 = cp4.join(cl4)
    jcp4 = jcp4[jcp4.Spread.notnull()]
    jcp4 = jcp4.drop(['exchange','symbol'],axis=1)
    jcp5 = cp5.join(cl5)
    jcp5 = jcp5[jcp5.Spread.notnull()]
    jcp5 = jcp5.drop(['exchange','symbol'],axis=1)
    jcp6 = cp6.join(cl6)
    jcp6 = jcp6[jcp6.Spread.notnull()]
    jcp6 = jcp6.drop(['exchange','symbol'],axis=1)
    jcp7 = cp7.join(cl7)
    jcp7 = jcp7[jcp7.Spread.notnull()]
    jcp7 = jcp7.drop(['exchange','symbol'],axis=1)
    jcp8 = cp8.join(cl8)
    jcp8 = jcp8[jcp8.Spread.notnull()]
    jcp8 = jcp8.drop(['exchange','symbol'],axis=1)
    jcp9 = cp9.join(cl9)
    jcp9 = jcp9[jcp9.Spread.notnull()]
    jcp9 = jcp9.drop(['exchange','symbol'],axis=1)
    
    joins = []
    joins.append(jcp1)
    joins.append(jcp2)
    joins.append(jcp3)
    joins.append(jcp4)
    joins.append(jcp5)
    joins.append(jcp6)
    joins.append(jcp7)
    joins.append(jcp8)
    joins.append(jcp9)
    
    return joins

def EffectiveSpread(me3):

    inst = ['ETH/USD','SOL/USD','BTC/USD']
    exch = ['Bitso', 'Gate', 'Okcoin']

    lista_activos = []

    for i in range(3):

        for j in range(3):

            lista_es = []
            cp1 = me3[(me3["exchange"] == exch[i]) & (me3["symbol"] == inst[j])]
            fechas_es = cp1.timestamp2.unique()

            for k in range(len(fechas_es)):

                cp1 = cp1[(cp1["timestamp2"] == fechas_es[k])]

                cp1["Pt"] = cp1.iloc[:,9].shift() - cp1.iloc[:,9]
                cp1["Pt"] = cp1["Pt"].fillna(0)
                cp1["Pt-5"] = cp1.iloc[:,9].shift(5) - cp1.iloc[:,9].shift(4)
                cp1["Pt-5"] = cp1["Pt-5"].fillna(0)

                cov = np.abs(np.cov(cp1["Pt"],cp1["Pt-5"]))
                cov_value = cov[0][1]
                es = np.sqrt(cov_value)*2
                lista_es.append(es)
                cp1 = me3[(me3["exchange"] == exch[i]) & (me3["symbol"] == inst[j])]

            lista_activos.append(lista_es)

    return lista_activos

def ESR(ppp, es):
    lista_act2 = []
    for i in range(9):
        ppp[i]["Effective"] = es[i]
        num = ppp[i]
        lista_act2.append(num)
    return lista_act2

def Salidas(lista):
    SSS = []
    Salida_B1 = lista[0][['CP ETH/USD Bitso','Spread','Effective']]
    Salida_B2 = lista[1][['CP SOL/USD Bitso','Spread','Effective']]
    Salida_B3 = lista[2][['CP BTC/USD Bitso','Spread','Effective']]
    Salida_B4 = lista[3][['CP ETH/USD Gate.io','Spread','Effective']]
    Salida_B5 = lista[4][['CP SOL/USD Gate.io','Spread','Effective']]
    Salida_B6 = lista[5][['CP BTC/USD Gate.io','Spread','Effective']]
    Salida_B7 = lista[6][['CP ETH/USD OKCoin','Spread','Effective']]
    Salida_B8 = lista[7][['CP SOL/USD OKCoin','Spread','Effective']]
    Salida_B9 = lista[8][['CP BTC/USD OKCoin','Spread','Effective']]
    S1 = pd.concat([Salida_B1,Salida_B4,Salida_B7],axis=1)
    S2 = pd.concat([Salida_B2,Salida_B5,Salida_B8],axis=1)
    S3 = pd.concat([Salida_B3,Salida_B6,Salida_B9],axis=1)
    SSS.append(S1)
    SSS.append(S2)
    SSS.append(S3)
    return SSS