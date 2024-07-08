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
    balance = exchange.fetch_balance()
    return balance[type]

def bullCalculator(exchange, tickerList):
    bullCnt = 0
    bearCnt = 0
    bullTickerList = []
    bearTickerList = []
    tickers = exchange.fetch_tickers()
    import pprint
    pprint.pprint(tickers)
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
        print('returning BearTickerList')
        return 'sell', bearTickerList
    else :
        print('returning BullTickerList')
        return 'buy', bullTickerList
