import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout="centered")
st.title("Vanilla Options")
st.header('General feature of options')
st.text("Contrat entre deux parties, qui donne aux acheteurs un droit mais pas une obligation \n"
        "d'acheter ou de vendre un actif a un certain prix, certain call contain a physical delivery features, witch"
        "mean that the call seller or the put buyer will deliver the stock at mat when the call is exercised")

st.table(
    pd.DataFrame.from_dict({'ATM at the money': 'St = K', 'ITM in the money': 'St > K', 'OTM out the money ': 'St < K'},
                           orient='index', columns=['']))
st.header('Call and options payoffs')

st.subheader('CALL')
st.text('Le Call correspond à une vue Bearish du marché cad le St sera au dessus de K à matu')
st.latex("call  =  n * max[0,St  -  K]")
st.image(Image.open("img/singleStockAndOptions_call.JPG"), 'call payoff')

st.subheader('PUT')
st.latex("put  =  n * max[0,K  -  s]")
st.image(Image.open("img/singleStockAndOptions_put.JPG"), 'put payoff')


tab_list = ['call_put_parity','BS_MODEL_ASSUMPTION']
tab = st.tabs(tab_list)

for tab_name,tab in zip(tab_list,tab):
    with tab:
        if tab_name == 'call_put_parity':
            st.markdown('it is the relation between call and put options with same K and same mat,'
                        'to explain this relation with must assume that both of them are european.'
                        'A violation of this rule lead to arbitrage opportunities. The relation is given by :')
            st.latex('Call(K,T) + Ke^{-rt} = Put(K,T) + Soe^{-qt}')
            st.markdown('r and q are respectively the risk free rate and the dividend yield')
            st.markdown('Ptf A = long one call and short one put same K same S same mat')
            st.markdown('Ptf B = long forward (obligation to buy)')
            st.markdown('At mat both ptf must have the same payoffs, therefore their present value must be the same'
                        'otherwise and investor can arbitrage and make risk profit buy purchasing the less expensive ptf')
        elif tab_name == 'BS_MODEL_ASSUMPTION':
            st.markdown('In 1973 Fischer Black and Myron Scholes published Black and Scholes, it is a pricing formula for european options')
            st.title('Model assumption')
            st.markdown('- Vol of udl is constant over time')
            st.markdown('- Udl can be traded continuously and the price is log-normaly distributed,'
                        'Therefore the log returns of S are log normal')
            st.markdown('- We can always short cell the underlying stock')
            st.markdown('- There is no transaction cost or taxes')
            st.markdown('- All securities are perfectly divisible')
            st.markdown('- Constant interest rate')
            st.markdown('- Constant dividend')

            st.subheader('Risk-Neutral-Pricing')
            st.markdown('Concider a scenario where you have a choice between receiving 1 dollar or receiving 2 dollar'
                        'with 50% chance, The risk averse investor will chose 1 dollar; whereas the risk seeking one will take'
                        'the 2 dollar, the risk neutral investor has no preference')
            st.markdown('In finance, when pricing an asset; we figure the proba of future cashflow and then discount it'
                        'at the free risk rate. For instance if the proba of receiving two dollar is 50% from know, the value is 1 dollar'
                        'This is called the expected value. In the theory of risk neutral pricing the real world proba assigned to future cashflow are irrelevant'
                        'and we must obtain risk neutral probability')
            st.markdown('The goal of risk neutral valuation is to use a replicating portofolio with known prices to remove any risk. The amount of asset neeeded'
                        'determine the risk-neutral proba, In BS we concider that one can replicate the payoff with the stock itself and risk free bonds '
                        'It is therefore preference free because options can be replicated and thus their theorical value do not depend upon investor'
                        '')

        elif tab_name == 'Pricing a european call option':
            with st.expander("C'EST KOA UN LOG ?"):
                st.write("""
                    Le logarithme naturel ou logarithme népérien, ou encore logarithme hyperbolique jusqu'au xxe siècle, transforme,
                     comme les autres fonctions logarithmes, les produits en sommes. L'utilisation de telles fonctions permet de 
                     faciliter les calculs comprenant de nombreuses multiplications, divisions et élévations à des puissances
                      rationnelles. Il est souvent noté ln(). Le logarithme naturel ou népérien est dit de base e car ln(e) = 1..
                """)
                st.image("https://upload.wikimedia.org/wikipedia/commons/8/88/Logarithme_n%C3%A9p%C3%A9rien.png",
                         "https://fr.wikipedia.org/wiki/Logarithme_naturel")

            st.header('')
            st.text(r"""
            C = Call option price 
            S = Current stock price
            K = Strike price of the option
            r = risk-free interest rate (a number between 0 and 1)
            sigma = volatility of the stocks return (a number between 0 and 1)
            t = time to option maturity (in years)
            N = normal cumulative distribution function""")

            st.caption("BS formula for European Call:")
            st.latex(
                r"""\mathrm C(\mathrm S,\mathrm t)= \mathrm N(\mathrm d_1)\mathrm S - \mathrm N(\mathrm d_2) \mathrm K \mathrm e^{-rt}""")
            col1, col2, col3, col4 = st.columns(4)

            col1.latex(r"""
            d_{1}=\frac{\ln \frac{S_{t}}{K} + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}
            """)

            col4.latex(r"""d_{2}=d_{1}-\sigma\sqrt{\tau}""")
            st.markdown('the payoff of a call is also known as intrasic value in other word, the value of exercicing the call now'
                        'the call price is always above the intrasic value, the difference between them is the time value.'
                        'The time value is the materialization of the uncertnity of finishing in the money, it is always positive and '
                        'the max is when St = K')

        elif tab_name == 'Pricing a european Put option':
            st.latex(
                r"""\mathrm P(\mathrm S,\mathrm t)= \mathrm N(\mathrm d_1 -1)\mathrm S - \mathrm N(\mathrm d_2 -1) \mathrm K \mathrm e^{-rt}""")
            st.markdown('Time value of a put can be neg ITM')
        elif tab_name == 'The cost of hedging':
            st.markdown('The price BS generate should be a reflection of the cost of hedging the option. When a trader '
                        'sell an option he charge a premium for the risk he is bearing')
            with st.expander(label="Stock Alpha can take two value 120 and 70 after 5 year, Spot init is 100."
                                   "The analysis show that there is 60% chance that the spot end to be 120 and "
                                   "40% that it will be 70. What would be the fair price of a 5 year european "
                                   "ATM call"):
                st.markdown('if you short the call you have to be long delta in order to cover spot price variation')
                st.markdown("C is the call premium that you earn if the finish price is 120 then "
                            "PnL = -20 + 20Δ + C = 0 if the price end to be 70 then "
                            "PnL = 0 -30Δ + C = 0"
                            )
                st.markdown('If we solve the equation we find Δ=40% and C=12')