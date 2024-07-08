import time
import lib
import trade
import assessment

def main():
    exchange = lib.connectBinance()
    tickers = exchange.fetch_tickers()
    symbols = tickers.keys()
    usdt_symbols = [x for x in symbols if x.endswith('USDT')] 
    while True:
        assetList = assessment.assessPortfolio(exchange=exchange)
        if len(assetList) == 0:
            print('Re-evaluating...')
            buyOrSell, tradeList = lib.bullCalculator(exchange=exchange, tickerList=usdt_symbols)
            boughtList = trade.buildOrder(exchange=exchange, tickerList=tradeList, buy=buyOrSell, dollarAmount=10, leverage=2)
            print('다음의 코인 선물을 거래함.')
            print(list(bought['ticker'] for bought in boughtList))
        else :
            stopLossList = assessment.getStopLossList(assetList, limit=-0.05)
            checkCloseFlag = assessment.checkClose(assetList=assetList, limit=0.10)
            if len(stopLossList) > 0:
                assessment.closeAssets(exchange=exchange, assetList=stopLossList)
                print('다음의 코인을 손절함.')
                print(stopLossList)
            elif checkCloseFlag == True:
                assessment.closeAssets(exchange=exchange, assetList=assetList)
                print('모든 코인 청산함.')
            
        time.sleep(10)

main()