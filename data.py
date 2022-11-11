# python script for data collection

import functions as fn
import ccxt
import pandas as pd 
import numpy as np

# Exchanges

#bitstamp = ccxt.bitstamp()
bitso = ccxt.bitso()
#alpaca = ccxt.alpaca()
#ascendex = ccxt.ascendex()
okcoin = ccxt.okcoin()
gate = ccxt.gate()
exc = [bitso,gate,okcoin]
inst = ['ETH/USD','SOL/USD','BTC/USD']
exchl = ['Bitso','Gate','Okcoin']


