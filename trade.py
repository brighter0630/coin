def buildOrder(exchange, tickerList, leverage, buy, dollarAmount):
    buyOrSell = "buy" if buy == "buy" else "sell" 
    sortedList = sorted(tickerList, key=lambda x: -abs(x['percentage']))
    boughtList = []
    for ticker in sortedList:
        try:
            amount = dollarAmount*leverage/ticker['close']
            exchange.set_leverage(leverage, ticker['ticker'])
            exchange.create_order(
                symbol = ticker['ticker'], 
                type="MARKET",
                side=buyOrSell,
                amount=amount
            )
            boughtList.append(ticker)
        except:
            pass

    return boughtList