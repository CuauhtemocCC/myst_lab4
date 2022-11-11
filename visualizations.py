# python script with data visualization functions

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def grafos(tabla):
    #tabla = microestructura_tabla
    fig = make_subplots(
        rows=3,cols=3,shared_xaxes=True,vertical_spacing=0.02,shared_yaxes=True,horizontal_spacing=0.02)

    fig.add_trace(go.Scatter(name="Bitso ETH/USD",
                             x=tabla[(tabla["exchange"] == 'Bitso') & (tabla["symbol"] == 'ETH/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Bitso') & (tabla["symbol"] == 'ETH/USD')].iloc[:,8]),
                  row=1,col=1)
    fig.add_trace(go.Scatter(name="Bitso SOL/USD",
                             x=tabla[(tabla["exchange"] == 'Bitso') & (tabla["symbol"] == 'SOL/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Bitso') & (tabla["symbol"] == 'SOL/USD')].iloc[:,8]),
                  row=2,col=1)
    fig.add_trace(go.Scatter(name="Bitso BTC/USD",
                             x=tabla[(tabla["exchange"] == 'Bitso') & (tabla["symbol"] == 'BTC/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Bitso') & (tabla["symbol"] == 'BTC/USD')].iloc[:,8]),
                  row=3,col=1)

    fig.add_trace(go.Scatter(name="Gate ETH/USD",
                             x=tabla[(tabla["exchange"] == 'Gate') & (tabla["symbol"] == 'ETH/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Gate') & (tabla["symbol"] == 'ETH/USD')].iloc[:,8]),
                  row=1,col=2)
    fig.add_trace(go.Scatter(name="Gate SOL/USD",
                             x=tabla[(tabla["exchange"] == 'Gate') & (tabla["symbol"] == 'SOL/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Gate') & (tabla["symbol"] == 'SOL/USD')].iloc[:,8]),
                  row=2,col=2)
    fig.add_trace(go.Scatter(name="Gate BTC/USD",
                             x=tabla[(tabla["exchange"] == 'Gate') & (tabla["symbol"] == 'BTC/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Gate') & (tabla["symbol"] == 'BTC/USD')].iloc[:,8]),
                  row=3,col=2)

    fig.add_trace(go.Scatter(name="Okcoin ETH/USD",
                             x=tabla[(tabla["exchange"] == 'Okcoin') & (tabla["symbol"] == 'ETH/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Okcoin') & (tabla["symbol"] == 'ETH/USD')].iloc[:,8]),
                  row=1,col=3)
    fig.add_trace(go.Scatter(name="Okcoin SOL/USD",
                             x=tabla[(tabla["exchange"] == 'Okcoin') & (tabla["symbol"] == 'SOL/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Okcoin') & (tabla["symbol"] == 'SOL/USD')].iloc[:,8]),
                  row=2,col=3)
    fig.add_trace(go.Scatter(name="Okcoin BTC/USD",
                             x=tabla[(tabla["exchange"] == 'Okcoin') & (tabla["symbol"] == 'BTC/USD')].iloc[:,2],
                             y=tabla[(tabla["exchange"] == 'Okcoin') & (tabla["symbol"] == 'BTC/USD')].iloc[:,8]),
                  row=3,col=3)

    fig.update_xaxes(title_text=exchl[0], row=3,col=1)
    fig.update_xaxes(title_text=exchl[1], row=3,col=2)
    fig.update_xaxes(title_text=exchl[2], row=3,col=3)

    fig.update_yaxes(title_text="ETH/USD", row=1,col=1)
    fig.update_yaxes(title_text="SOL/USD", row=2,col=1)
    fig.update_yaxes(title_text="BTC/USD", row=3,col=1)


    fig.update_layout(height=600,
                      title_text="Exchanges")

    return fig.show()