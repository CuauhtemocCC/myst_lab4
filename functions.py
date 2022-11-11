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

def microestructura(inst,limite,t,exc):
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

