import streamlit as st
import pandas as pd

st.title('DELTA')
with st.expander("Δ"):
    st.header('definition')
    st.markdown(
        "Delta is the rate of change of the option price with respect to the price of"
        "the underlying asset. It measures the first-order sensitivity of the price "
        "to a movement in stock price S. The option delta is 0.4 means that if "
        "the underlying moves by for example 1%, then the value of the option will"
        "move by 0.4 × 1%. For European options on an asset that provides a yield at rate q:")


    st.latex(r"delta(call)=\frac{\partial c}{\partial S}=e^{-q(T-t)}N(d1)")
    st.latex(r"delta(put)=\frac{\partial p}{\partial S}=e^{-q(T-t)}(N(d1)-1)")

    st.caption("impact factors :")
    st.table(
        pd.DataFrame.from_dict({
            'Stock Price ': 'all option has a positive Delta range from 0 to 1. The Delta is positively correlated to underlying stock price change'
            ,
            'Implied Volatility ': 'Low implied volatility stocks will tend to have higher Delta for the in-the-money options and lower Delta for out-of-the-money options.',
            'Days remaining to expiration ': 'As expiration nears, in-the-money call Deltas increase toward 1.00, at-the-money call Deltas remain at around 0.5 and out-of-the-money call Deltas fall to 0 provided other inputs remain constant.'},
            orient='index', columns=['']))
