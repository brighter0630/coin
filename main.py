import pandas as pd
import lib
import trade
import pprint

exchange = lib.connectBinance()
markets = exchange.load_markets()
tickers = exchange.fetch_tickers()
symbols = tickers.keys()
usdt_symbols = [x for x in symbols if x.endswith('USDT')]
balance = lib.getBalance(exchange, 'USDT')

buyOrSell, tradeList = lib.bullCalculator(exchange, symbols)
trade.tradeOrder(exchange, tradeList, leverage=3, buy=buyOrSell, dollarAmount=10)