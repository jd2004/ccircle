# Your solution goes in this file!

'''
  --- ACCOUNT ------------------------------------------------------------------

    account.getBalance() -> Real Number

      Get the amount of money in your account

    account.getShares(sym) -> Integer

      Get the number of shares of the given stock that you currently own

  --- MARKET -------------------------------------------------------------------

    market.buy(account, sym, quantity) -> None

      Buy 'quantity' shares of the stock with symbol 'sym' using 'account'
      You must have enough money in your account or the function will fail!

    market.getPrice(sym) -> Real Number

      Return the current price of the given stock

    market.getHistory(sym) -> List

      Return a list of historical prices for the given stock

    market.getStockSymbols() -> List

      Return a list of all the stock symbols

    market.sell(account, sym, quantity) -> None

      Sell 'quantity' shares of the stock with symbol 'sym' using 'account'
      You must have enough shares in your account or the function will fail!
'''

class StockTrader:
    def __init__(self):
        # Set variables if you want
        pass

    # Controls how difficult the simulation is:
    #    0.0 -> easiest
    #    0.5 -> moderate
    #    1.0 -> hardest
    def getDifficulty(self):
        return 1.0

    # Controls how fast the simulation runs; 0 = fastest
    def getPauseTime(self):
        return 0.0

    # Use different numbers to get different random variations of the simulation
    def getSeed(self):
        return 1337


    # Analyze the market for the current day and make trades as you see fit. Try to make as much money as you can!
    def trade(self, account, market):
        # This is a very basic and bad starter strategy: get a list of stocks, buy any stock that is less than $10
        # (if we can afford it); sell any stock that is more than $20 (if we own it). You must do better than this!
        t=0
        syms = market.getStockSymbols()
        for sym in syms:
            price = market.getPrice(sym)
            t+=1
            if account.getShares(sym) > 0 and 45+t < price:
                market.sell(account, sym, 1)
            elif account.getBalance() >= 750+t*50:
                if price < 30+t:
                    market.buy(account, sym, 20)
                elif price < 35+t:
                    market.buy(account, sym, 10)
                elif price < 40+t:
                    market.buy(account, sym, 8)
            print(t)
        # Test change 2
