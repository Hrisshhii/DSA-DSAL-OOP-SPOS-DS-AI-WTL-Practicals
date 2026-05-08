class Stock:

    def __init__(self, name, price, trend, volume, rsi):

        self.name = name
        self.price = price
        self.trend = trend.lower()
        self.volume = volume.lower()
        self.rsi = rsi.lower()

        self.decision = ""
        self.risk = ""
        self.suggestion = ""


class StockExpertSystem:

    def analyze(self, stock):

        if (stock.trend == "bullish" and
            stock.volume == "high" and
            stock.rsi == "normal"):

            stock.decision = "BUY"
            stock.risk = "Low"
            stock.suggestion = "Strong upward momentum."


        elif (stock.trend == "bullish" and
              stock.rsi == "overbought"):

            stock.decision = "HOLD"
            stock.risk = "Medium"
            stock.suggestion = "Wait for price dip."


        elif (stock.trend == "bearish" and
              stock.volume == "high"):

            stock.decision = "SELL"
            stock.risk = "High"
            stock.suggestion = "Downtrend confirmed."


        elif stock.rsi == "oversold":

            stock.decision = "BUY"
            stock.risk = "Medium"
            stock.suggestion = "Possible reversal."


        else:

            stock.decision = "HOLD"
            stock.risk = "Unknown"
            stock.suggestion = "Insufficient data."


    def display(self, stock):

        print("\n--- Stock Analysis ---")

        print("Stock Name:", stock.name)
        print("Price:", stock.price)

        print("Trend:", stock.trend)
        print("Volume:", stock.volume)
        print("RSI:", stock.rsi)

        print("Decision:", stock.decision)
        print("Risk Level:", stock.risk)

        print("Suggestion:", stock.suggestion)


# Main
system = StockExpertSystem()

name = input("Enter Stock Name: ")

price = float(input("Enter Price: "))

trend = input("Enter Trend (bullish/bearish/neutral): ")

volume = input("Enter Volume (high/low): ")

rsi = input("Enter RSI (normal/overbought/oversold): ")

stock = Stock(name, price, trend, volume, rsi)

system.analyze(stock)

system.display(stock)
