from tools.BS import BSOption
import streamlit as st
import numpy as np


class Plot:
    def get_CP(self):
        '''
        Get the Call or Put entry
        '''
        CP = str(st.session_state.call_or_put)
        if CP not in ["C", "P"]:
            # Returns error if neither "C" nor "P" is entered
            st.error("Option type error Enter either 'C' or 'P' in the Call/Put field", icon="🚨")
        else:
            return CP

    def get_K(self):
        '''
        Get the Strike price entry
        '''
        try:
            K = float(st.session_state.strike_price)
            if K < 1:
                # Returns error if a negative strike price is entered
                st.error("Strike value error Enter at least a strike price equal to 1", icon="🚨")
            else:
                return K
        except:
            st.error("Strike value error Enter a valid strike price", icon="🚨")

    def get_T(self):
        '''
        Get the Maturity entry
        '''
        try:
            if "maturity_twister" in st.session_state:
                T = float(st.session_state.maturity_twister)
            else:
                T = float(st.session_state.maturity)
            if T < 0:
                # Returns error if a negative maturity is entered
                st.error("Maturity value error Enter a maturity at least equal to 0 (expiration)", icon="🚨")
            elif T > 5:
                # Returns a maximum maturity of 5 years
                st.error("Maturity value error Enter a maturity at least equal to 5 (years)", icon="🚨")
            else:
                return T
        except:
            st.error("Maturity value error Enter a valid maturity value (between 0 and 5 years)", icon="🚨")

    def get_r(self):
        '''
        Get the Interest Rate entry
        '''
        try:
            if "rate_twister" in st.session_state:
                r = float(st.session_state.rate_twister)
            else:
                r = float(st.session_state.interest_rate)
            if r < 0.01:
                # Returns a mininum of 0.01% (1 basis point)
                st.error("Interest Rate value error Enter at least an interest rate equal to 0.01(%)", icon="🚨")
            elif r > 10:
                # Returns a maximum interest rate of 10% (1000 basis point)
                st.error("Interest Rate value error Enter at least an interest rate equal to 10(%)", icon="🚨")
            else:
                return r / 100
        except:
            st.error("Interest Rate value error Enter a valid interest rate value (between 0.01% and 10%)", icon="🚨")

    def get_v(self):
        '''
        Get the Volatility entry
        '''
        try:
            if "volatility_twister" in st.session_state:
                v = float(st.session_state.volatility_twister)
            else:
                v = float(st.session_state.volatility)
            if v < 1:
                # Returns a mininum volatility of 1%
                st.error("Volatility value error Enter at least a volatility equal 1(%)", icon="🚨")
            elif v > 100:
                # Return a maximum volatility of 100%
                st.error("Volatility value error Enter at least a volatility equal 100(%)", icon="🚨")
            else:
                return v / 100
        except:
            st.error("Volatility value error Enter a valid volatility value (between 1% and 100%)", icon="🚨")

    def get_q(self):
        '''
        Get the Dividend Yield entry
        '''
        try:
            q = float(st.session_state.dividend_yield)
            if q < 0:
                # If a negative dividend yield is entered, then return 0
                st.error("Dividend Yield value error vEnter at least a dividend yield equal 0(%)", icon="🚨")
            else:
                return q
        except:
            st.error("Dividend Yield value error Enter a valid dividend yield value", icon="🚨")

    @staticmethod
    def get_Smin(K):
        '''
        Automatic generation of a minimum underlying price (for plot)
        calculated as 60% below the input strike price
        '''
        return round(K * (1 - 0.60), 0)

    @staticmethod
    def get_Smax(K):
        '''
        Automatic generation of a maximum underlying price (for plot)
        calculated as 60% above the input strike price
        '''
        return round(K * (1 + 0.60), 0)

    @staticmethod
    def get_Sset(Smin, Smax):
        '''
        Generation of 150 underlying prices for the plots
        '''
        return np.linspace(Smin, Smax, 150)

    def computeoption(self):
        '''
        Calculate option price and greeks given the input data
        '''
        # Recover inserted data
        self.CP = self.get_CP()
        self.K = self.get_K()
        self.T = self.get_T()
        self.r = self.get_r()
        self.v = self.get_v()
        self.q = self.get_q()
        self.Smin = self.get_Smin(self.K)
        self.Smax = self.get_Smax(self.K)
        self.Sset = self.get_Sset(self.Smin, self.Smax)

        # Calculate Option
        self.option = [BSOption(self.CP,
                                s,
                                self.K,
                                self.T,
                                self.r,
                                self.v,
                                q=self.q) for s in self.Sset]
        ...
