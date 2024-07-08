import pandas as pd
import lib
import trade

exchange = lib.connectBinance()
markets = exchange.load_markets()
tickers = exchange.fetch_tickers()
symbols = tickers.keys()
usdt_symbols = [x for x in symbols if x.endswith('USDT')]
balance = lib.getBalance(exchange, 'USDT')

buyOrSell, tradeList = lib.bullCalculator(exchange, symbols)
boughtList = trade.buildOrder(exchange, tradeList, leverage=2, buy=buyOrSell, dollarAmount=10)
print(bought['symbol'] for bought in boughtList)