from tools.BS_opt_strat import BSOptStrat


class strat_builder:

    def __init__(self, s, q, r, t):
        self.S = s
        self.Q = q
        self.R = r
        self.T = t

        # Set of pre-defined option strategies
        self.strat_options = ("Custom strategy",
                              "Long Call",
                              "Short Call",
                              "Long Put",
                              "Short Put",
                              "Bull Call Spread",
                              "Bull Put Spread",
                              "Bear Call Spread",
                              "Bear Put Spread",
                              "Top Strip",
                              "Bottom Strip",
                              "Top Strap",
                              "Bottom Strap",
                              "Top Straddle",
                              "Bottom Straddle",
                              "Top Strangle",
                              "Bottom Strangle",
                              "Top Butterfly",
                              "Bottom Butterfly",
                              "Top Iron Condor",
                              "Bottom Iron Condor")

        # Chosen strategy (custom or predefined)
        self.chosen_strategy = None

    def get_S(self):
        '''
        Get the Underlying price entry
        '''
        try:
            S = float(self.S)
            if S <= 0:
                # Returns error if a negative or zero Underlying price is entered
                print("Underlying price error", "Enter a positive Underlying price")
            else:
                return S
        except:
            print("Underlying value error", "Enter a valid Underlying price")

    def get_r(self):
        '''
        Get the Interest Rate entry
        '''
        try:
            r = float(self.R)
            if r < 0.01:
                # Returns a mininum of 0.01% (1 basis point)
                print("Interest Rate value error", "Enter at least an interest rate equal to 0.01(%)")
            elif r > 10:
                # Returns a maximum interest rate of 10% (1000 basis point)
                print("Interest Rate value error", "Enter at least an interest rate equal to 10(%)")
            else:
                return r / 100
        except:
            print("Interest Rate value error",
                  "Enter a valid interest rate value (between 0.01% and 10%)")

    def get_q(self):
        '''
        Get the Dividend Yield entry
        '''
        try:
            q = float(self.Q)
            if q < 0:
                # If a negative dividend yield is entered, then return 0
                print("Dividend Yield value error", "Enter at least a dividend yield equal 0(%)")
            else:
                return q
        except:
            print("Dividend Yield value error", "Enter a valid dividend yield value")

    def get_T(self):
        '''
        Get the Maturity entry
        '''
        try:
            T = float(self.T)
            if T < 0:
                # Returns error if a negative maturity is entered
                print("Maturity value error", "Enter a maturity at least equal to 0 (expiration)")
            elif T > 5:
                # Returns a maximum maturity of 5 years
                print("Maturity value error", "Enter a maturity at least equal to 5 (years)")
            else:
                return T
        except:
            print("Maturity value error", "Enter a valid maturity value (between 0 and 5 years)")

    def get_selected_strategy(self, selection):
        '''
        Recover the option strategy selected from the main drop-down menu
        '''
        self.S = self.get_S()
        self.r = self.get_r()
        self.q = self.get_q()
        self.T = self.get_T()

        self.chosen_strategy = selection

        # Create strategy class with the underlying price, the time-to-maturity, and the dividend yield
        self.Strategy = BSOptStrat(S=self.S, r=self.r, q=self.q)

        # Auxiliary increase/decrese for strike prices in the pre-defined strategies (according to current level of the underlying price)
        dS = 5 / 100

        # Auxiliary increase/decrese for strike prices in the pre-defined strategies (according to current level of the underlying price)
        # Naked
        if self.chosen_strategy == "Long Call":
            # Long Call (ATM option)
            self.Strategy.call(NP=1, K=self.S, T=self.T, v=30 / 100)

        elif self.chosen_strategy == "Short Call":
            # Short Call (ATM option)
            self.Strategy.call(NP=-1, K=self.S, T=self.T, v=30 / 100)

        elif self.chosen_strategy == "Long Put":
            # Long Put (ATM option)
            self.Strategy.put(NP=+1, K=self.S, T=self.T, v=30 / 100)

        elif self.chosen_strategy == "Short Put":
            # Short Put (ATM option)
            self.Strategy.put(NP=-1, K=self.S, T=self.T, v=30 / 100)


        # Bull Spreads

        elif self.chosen_strategy == "Bull Call Spread":
            # Bull Call Spread
            # - 1 long ITM call (K<S)
            # - 1 short OTM call (K>S)
            self.Strategy.call(NP=1, K=self.S * (1 - dS), T=self.T, v=30 / 100)
            self.Strategy.call(NP=-1, K=self.S * (1 + dS), T=self.T, v=20 / 100)

        elif self.chosen_strategy == "Bull Put Spread":
            # Bull Put Spread
            # - 1 long OTM put (K<S)
            # - 1 short ITM put (K>S)
            self.Strategy.put(NP=1, K=self.S * (1 - dS), T=self.T, v=30 / 100)
            self.Strategy.put(NP=-1, K=self.S * (1 + dS), T=self.T, v=20 / 100)


        # Bear Spreads

        elif self.chosen_strategy == "Bear Call Spread":
            # Bear Call Spread
            # - 1 long OTM call (K>S)
            # - 1 short ITM call (K<S)
            self.Strategy.call(NP=1, K=self.S * (1 + dS), T=self.T, v=20 / 100)
            self.Strategy.call(NP=-1, K=self.S * (1 - dS), T=self.T, v=30 / 100)

        elif self.chosen_strategy == "Bear Put Spread":
            # Bear Put Spread
            # - 1 long ITM put (K>S)
            # - 1 short OTM put (K<S)
            self.Strategy.put(NP=1, K=self.S * (1 + dS), T=self.T, v=20 / 100)
            self.Strategy.put(NP=-1, K=self.S * (1 - dS), T=self.T, v=30 / 100)


        # Straps

        elif self.chosen_strategy == "Top Strip":
            # Top Strip (asymmetric straddle)
            # - 1 short call
            # - 2 short put
            # at the same strike price
            self.Strategy.call(NP=-1, K=self.S, T=self.T, v=25 / 100)
            self.Strategy.put(NP=-2, K=self.S, T=self.T, v=25 / 100)

        elif self.chosen_strategy == "Bottom Strip":
            # Bottom Strip (asymmetric straddle)
            # - 1 long call
            # - 2 long put
            # at the same strike price
            self.Strategy.call(NP=+1, K=self.S, T=self.T, v=25 / 100)
            self.Strategy.put(NP=+2, K=self.S, T=self.T, v=25 / 100)


        # Strips

        elif self.chosen_strategy == "Top Strap":
            # Top Strap (asymmetric straddle)
            # - 2 short call
            # - 1 short put
            # at the same strike price
            self.Strategy.call(NP=-2, K=self.S, T=self.T, v=25 / 100)
            self.Strategy.put(NP=-1, K=self.S, T=self.T, v=25 / 100)

        elif self.chosen_strategy == "Bottom Strap":
            # Bottom Strap (asymmetric straddle)
            # - 2 long call
            # - 1 long put
            # at the same strike price
            self.Strategy.call(NP=+2, K=self.S, T=self.T, v=25 / 100)
            self.Strategy.put(NP=+1, K=self.S, T=self.T, v=25 / 100)


        # Straddles

        elif self.chosen_strategy == "Top Straddle":
            # Top Straddle
            # - 1 short call
            # - 1 short put
            # at the same strike price
            self.Strategy.call(NP=-1, K=self.S, T=self.T, v=25 / 100)
            self.Strategy.put(NP=-1, K=self.S, T=self.T, v=25 / 100)

        elif self.chosen_strategy == "Bottom Straddle":
            # Bottom Straddle
            # - 1 long call
            # - 1 long put
            # at the same strike price
            self.Strategy.call(NP=+1, K=self.S, T=self.T, v=25 / 100)
            self.Strategy.put(NP=+1, K=self.S, T=self.T, v=25 / 100)


        # Strangles

        elif self.chosen_strategy == "Top Strangle":
            # Top Strangle
            # - 1 short call
            # - 1 short put
            # at different strike prices
            self.Strategy.call(NP=-1, K=self.S * (1 + dS), T=self.T, v=20 / 100)
            self.Strategy.put(NP=-1, K=self.S * (1 - dS), T=self.T, v=30 / 100)

        elif self.chosen_strategy == "Bottom Strangle":
            # Bottom Strangle
            # - 1 long call
            # - 1 long put
            # at different strike prices
            self.Strategy.call(NP=+1, K=self.S * (1 + dS), T=self.T, v=20 / 100)
            self.Strategy.put(NP=+1, K=self.S * (1 - dS), T=self.T, v=30 / 100)


        # Butterflies

        elif self.chosen_strategy == "Top Butterfly":
            # Top Butterfly
            # - 1 long ITM call
            # - 1 long OTM call
            # - 2 short ATM call
            self.Strategy.call(NP=+1, K=self.S * (1 - dS * 2), T=self.T, v=30 / 100)
            self.Strategy.call(NP=+1, K=self.S * (1 + dS * 2), T=self.T, v=20 / 100)
            self.Strategy.call(NP=-2, K=self.S, T=self.T, v=25 / 100)

        elif self.chosen_strategy == "Bottom Butterfly":
            # Bottom Butterfly
            # - 1 short ITM call
            # - 1 short OTM call
            # - 2 long ATM call
            self.Strategy.call(NP=-1, K=self.S * (1 - dS * 2), T=self.T, v=30 / 100)
            self.Strategy.call(NP=-1, K=self.S * (1 + dS * 2), T=self.T, v=20 / 100)
            self.Strategy.call(NP=+2, K=self.S, T=self.T, v=25 / 100)


        # Iron Condors

        elif self.chosen_strategy == "Top Iron Condor":
            # Top Iron Condor
            # - Bull Put Spread:
            #   1 long put and 1 short put at different strikes,
            #   both smaller than the strikes of the Bear Call Spreads
            self.Strategy.put(NP=+1, K=self.S * (1 - dS * 2), T=self.T, v=30 / 100)
            self.Strategy.put(NP=-1, K=self.S * (1 - dS), T=self.T, v=25 / 100)
            # - Bear Call Spread:
            #   1 long call and 1 short call at different strikes
            self.Strategy.call(NP=+1, K=self.S * (1 + dS * 2), T=self.T, v=20 / 100)
            self.Strategy.call(NP=-1, K=self.S * (1 + dS), T=self.T, v=15 / 100)

        elif self.chosen_strategy == "Bottom Iron Condor":
            # Bottom Iron Condor
            # - Bear Put Spread:
            #   1 short put and 1 long put at different strikes,
            #   both smaller than the strikes of the Bear Call Spreads
            self.Strategy.put(NP=-1, K=self.S * (1 - dS * 2), T=self.T, v=30 / 100)
            self.Strategy.put(NP=+1, K=self.S * (1 - dS), T=self.T, v=25 / 100)
            # - Bull Call Spread:
            #   1 short call and 1 long call at different strikes
            self.Strategy.call(NP=-1, K=self.S * (1 + dS * 2), T=self.T, v=20 / 100)
            self.Strategy.call(NP=+1, K=self.S * (1 + dS), T=self.T, v=15 / 100)

    def strategy_description(self):
        '''
        Returns the description of the pre-defined strategy
        '''
        Desc = dict()

        if self.chosen_strategy == "Long Call":
            nrows = 2
            desc = '''By buying a Call, \
you hope that the underlying stock price will increase. 
You will pay the option premium to buy the option.'''

        elif self.chosen_strategy == "Short Call":
            nrows = 2
            desc = '''By writing a Call, \
you hope that the underlying stock price will decrease. 
You will receive the option premium by writing the option.'''

        elif self.chosen_strategy == "Long Put":
            nrows = 2
            desc = '''By buying a Put, \
you hope that the underlying stock price will decrease. 
You will pay the option premium to buy the option.'''

        elif self.chosen_strategy == "Short Put":
            nrows = 2
            desc = '''By writing a Put, \
you hope that the underlying stock price will increase. 
You will receive the option premium by writing the option.'''

        elif self.chosen_strategy == "Bull Call Spread":
            nrows = 3
            desc = '''A Bull Call Spread is made by buying a Call \
with a certain strike price 
and by selling a Call with a higher strike price. \
You hope that the underlying stock price will increase.
Unlike Bull Put Spreads, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Bull Put Spread":
            nrows = 3
            desc = '''A Bull Put Spread is made by buying a Put \
with a certain strike price 
and by selling a Put with a higher strike price. \
You hope that the underlying stock price will increase.
Unlike Bull Call Spreads, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Bear Call Spread":
            nrows = 3
            desc = '''A Bear Call Spread is made by buying a Call \
with a certain strike price 
and by selling a Call with a lower strike price. \
You hope that the underlying stock price will decrease.
Unlike Bear Put Spreads, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Bear Put Spread":
            nrows = 3
            desc = '''A Bear Put Spread is made by buying a Put \
with a certain strike price 
and by selling a Put with a lower strike price. \
You hope that the underlying stock price will decrease.
Unlike Bear Call Spreads, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Top Strip":
            nrows = 4
            desc = '''A Top Strip consists of one short position in one Call \
and two Puts with the same strike price.
You hope there wont' be a big underlying price move and consider a decrease to be more likely than an increase.
It is a kind of an asymmetric Top Straddle.
Unlike Bottom Strips, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Bottom Strip":
            nrows = 4
            desc = '''A Bottom Strip consists of one long position in one Call \
and two Puts with the same strike price.
You hope there will be a big underlying price move and consider a decrease to be more likely than an increase.
It is a kind of an asymmetric Bottom Straddle.
Unlike Top Strips, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Top Strap":
            nrows = 4
            desc = '''A Top Strap consists of two short positions in one Call \
and one Put with the same strike price.
You hope there wont' be a big underlying price move and consider an increase to be more likely than a decrease.
It is a kind of an asymmetric Top Straddle.
Unlike Bottom Straps, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Bottom Strap":
            nrows = 4
            desc = '''A Bottom Strap consists of two long positions in one Call \
and one Put with the same strike price.
You hope there will be a big underlying price move and consider an increase to be more likely than a decrease.
It is a kind of an asymmetric Bottom Straddle.
Unlike Top Straps, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Top Straddle":
            nrows = 4
            desc = '''A Top Straddle consists of one short position in one Call \
and one Put with the same strike price.
You hope there wont' be a big underlying price move and you are not sure in which direction the move will be.
It is a kind of a symmetric Top Strip (or Strap).
Unlike Bottom Straddles, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Bottom Straddle":
            nrows = 4
            desc = '''A Bottom Straddle consists of one short position in one Call \
and one Put with the same strike price.
You hope there will be a big underlying price move and you are not sure in which direction the move will be.
It is a kind of a symmetric Bottom Strip (or Strap).
Unlike Top Straddles, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Top Strangle":
            nrows = 4
            desc = '''A Top Strangle consists of one short Call \
at a certain strike price and one short Put with a lower strike price.
You hope there wont' be a big underlying price move and you are not sure in which direction the move will be.
This is a strategy similar to a Top Straddle.
Unlike Bottom Strangles, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Bottom Strangle":
            nrows = 4
            desc = '''A Bottom Strangle consists of one long Call \
at a certain strike price and one long Put with a lower strike price.
You hope there will be a big underlying price move and you are not sure in which direction the move will be.
This is a strategy similar to a Bottom Straddle.
Unlike Top Strangles, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Top Butterfly":
            nrows = 5
            desc = '''A Top Butterfly consists of one long Call with relative low strike price, \
a long Call with relative higher strike \
price, and two short Calls with a strike that is halfway between the strikes of the Calls.  
You hope there wont' be a big underlying price move and you are not sure in which direction the move will be.
This is a strategy similar to a Top Straddle but with limited losses.
Unlike Bottom Butterfly, this strategy requires an initial investment.'''

        elif self.chosen_strategy == "Bottom Butterfly":
            nrows = 5
            desc = '''A Bottom Butterfly consists of one short Call with relative low strike price, \
a short Call with relative higher strike \  
price, and two long Calls with a strike that is halfway between the strikes of the Calls.  
You hope there will be a big underlying price move and you are not sure in which direction the move will be.
This is a strategy similar to a Bottom Straddle even though profits are limited.
Unlike Top Butterfly, this strategy provides an initial positive up-front cash inflow.'''

        elif self.chosen_strategy == "Top Iron Condor":
            nrows = 5
            desc = '''A Top Iron Condor consits of a Bull (Call/Put) Spread \
and a Bear (Call/Put) Spread, 
with both strikes of the Bear Spread larger than those of the Bull Spread. 
You hope there wont' be a big underlying price move and you are not sure in which direction the move will be.
This is a strategy similar to a Top Strangle but with limited losses.'''

        elif self.chosen_strategy == "Bottom Iron Condor":
            nrows = 5
            desc = '''A Bottom Iron Condor consits of a Bear (Call/Put) Spread \
and a Bull (Call/Put) Spread, 
with both strikes of the Bull Spread larger than those of the Bear Spread. 
You hope there will be a big underlying price move and you are not sure in which direction the move will be.
This is a strategy similar to a Bottom Strangle even though profits are limited.'''

            # Save description and number of rows
        Desc["msg"] = desc
        Desc["nrows"] = nrows

        return Desc


if __name__ == "__main__":
    x = strat_builder(s=100, q=10, r=0.01, t=0.25)
    x.get_selected_strategy(selection="Bull Call Spread")
    print()
