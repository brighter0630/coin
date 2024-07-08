def tradeOrder(exchange, tickerList, leverage, buy, dollarAmount):
    buyOrSell = "buy" if buy == "buy" else "sell" 
    sortedList = sorted(tickerList, key=lambda x: -abs(x['percentage']))
    print(sortedList)
    for ticker in sortedList:
        try:
            amount = dollarAmount*leverage/ticker['close']
            print('다음의 주문 입력 중')
            print('ticker: ', ticker['ticker'])
            print('amount: ', amount)
            exchange.set_leverage(leverage, ticker['ticker'])
            exchange.create_order(
                symbol = ticker['ticker'], 
                type="MARKET",
                side=buyOrSell,
                amount=amount
            )
        except:
            print('주문이 실패하였습니다.')