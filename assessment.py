def assessPortfolio(exchange):
    result = exchange.fetch_balance()
    assetList = list(filter(lambda x: float(x['positionAmt']) != 0, result['info']['positions']))
    return assetList

def getProfitRatio(el):
    return float(el['unrealizedProfit'])/float(el['initialMargin'])

def getStopLossList(assetList, limit: float):
    return list(filter(lambda x: getProfitRatio(x) < limit, assetList))

def checkClose(assetList, limit:float):
    if(any(getProfitRatio(asset) > limit for asset in assetList)):
        return True
    return False

def closeAssets(exchange, assetList):
    for asset in assetList:
        if float(asset['positionAmt']) < 0:
            exchange.create_market_buy_order(
                symbol=asset['symbol'],
                amount=abs(float(asset['positionAmt'])),
                params={
                    'positionSide': 'BOTH'
                }
            )
        else :
            exchange.create_market_sell_order(
                symbol=asset['symbol'],
                amount=abs(float(asset['positionAmt'])),
                params={
                    'positionSide': 'BOTH'
                }
            )
