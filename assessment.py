import lib
import ccxt
import pprint

def assessPortfolio(exchange):
    result = exchange.fapiPrivatePositionrisk()
    pprint.pprint(result)

exchange = lib.connectBinance()

assessPortfolio(exchange=exchange)