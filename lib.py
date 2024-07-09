import ccxt

def connectBinance():
    with open('./secret.txt') as f:
        lines = f.readlines()
        api_key = lines[0].strip()
        api_secret = lines[1].strip()

    exchange = ccxt.binance(config={
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future'
        }
    })

    return exchange

def getBalance(exchange, type):
    return exchange.fetch_balance()[type]

def bullCalculator(exchange, tickerList):
    bullCnt, bearCnt = 0, 0
    bullTickerList, bearTickerList = [], []
    tickers = exchange.fetch_tickers()
    for ticker in tickerList:
        el = {
            'ticker': ticker,
            'close': tickers[ticker]['close'],
            'percentage': tickers[ticker]['percentage']
        }
        if tickers[ticker]['percentage'] > 0:
            bullCnt = bullCnt + 1
            bullTickerList.append(el) 
        else :
            bearCnt = bearCnt + 1
            bearTickerList.append(el) 

    print("bullCnt: ", bullCnt)
    print("bearCnt: ", bearCnt)

    if bullCnt > bearCnt :
        print('returning BearTickerList, 강세장에서 약했던 놈들을 Short 할거에요.')
        return 'sell', bearTickerList
    else :
        print('returning BullTickerList, 약세장에서 강했던 놈들을 Long 할거에요.')
        return 'buy', bullTickerList
