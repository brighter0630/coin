import datetime

def transaction(content:str, logType='none'):
    with open('./transaction.log', mode='a') as alog:
        logText = datetime.datetime.now().strftime('%c') + 'type: ', logType, content
        print(logText)
        alog.write(str(logText))

def stopLoss(content:str):
    with open('./stoploss.log', mode='a') as sllog:
        logText = datetime.datetime.now().strftime('%c') + ' ' + content
        print(logText)
        sllog.write(str(logText))
