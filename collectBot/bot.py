import pandas as pd
import sys, os
import pprint
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import lib

def main():
    exchange = lib.connectBinance()
    tickers = exchange.fetch_tickers()
    usdt_tickers = lib.getUSDTOnly(tickers)
    pprint.pprint(len(tickers.keys()))
    print(len(usdt_tickers))
    # df = pd.DataFrame(tickers['info'])

main()