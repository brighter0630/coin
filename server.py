import time
import lib
import trade
import assessment
import datetime
import logger

def main():
    exchange = lib.connectBinance()
    tickers = exchange.fetch_tickers()
    symbols = tickers.keys()
    lastTrTime = datetime.datetime.now() 
    usdt_symbols = [x for x in symbols if x.endswith('USDT')] 
    while True:
        assetList = assessment.assessPortfolio(exchange=exchange)
        if len(assetList) == 0:
            logger.transaction('Re-evaluating...')
            buyOrSell, tradeList = lib.bullCalculator(exchange=exchange, tickerList=usdt_symbols)
            boughtList = trade.buildOrder(exchange=exchange, tickerList=tradeList, buy=buyOrSell, dollarAmount=20, leverage=3)
            lastTrTime = datetime.datetime.now()
            logger.transaction('다음의 코인 선물 포지션을 설정함.')
            logger.transaction(str(list(bought['ticker'] for bought in boughtList)), logType = 'init')
        else :
            stopLossList = assessment.getStopLossList(assetList, limit=-0.10)
            checkCloseFlag = assessment.checkClose(assetList=assetList, limit=0.20)
            if len(stopLossList) > 0:
                assessment.closeAssets(exchange=exchange, assetList=stopLossList)
                logger.stopLoss('다음의 코인을 손절함.')
                logger.stopLoss(str(stopLossList))
            elif (checkCloseFlag) == True or (lastTrTime - datetime.datetime.now() > datetime.timedelta(hours=4)):
                assessment.closeAssets(exchange=exchange, assetList=assetList)
                print('모든 코인 청산함.')
            else:
                print(datetime.datetime.now().strftime('%c'), '경과관찰 중')
            
        time.sleep(10)

main()