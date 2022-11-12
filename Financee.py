def stocks(name, timeperiod):

    import yfinance as yf

    
    try:
        data = yf.Ticker("name").history(period = timeperiod)

        print(data.head())
    except:
        print("error")


stocks("TSLA", "5y")