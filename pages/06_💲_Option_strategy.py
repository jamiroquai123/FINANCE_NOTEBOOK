import streamlit as st
import altair as alt
from tools.strat_builder import strat_builder
from tools.w_params import *


def load_data():
    st.session_state.plot = True
    st.session_state.strike_price = 100
    st.session_state.volatility = 1
    x = strat_builder(s=st.session_state.underlying_price, q=st.session_state.dividend_yield,
                      r=st.session_state.interest_rate, t=st.session_state.maturity)
    x.get_selected_strategy(selection=st.session_state.strat)
    st.session_state.simple_payoff = x.Strategy.payoffs_exp_df.reset_index().melt('index', var_name='ticker',
                                                                                  value_name="Price")
    st.session_state.aggregated_payoff = x.Strategy.payoffs_exp.reset_index().melt('index', var_name='ticker',
                                                                                   value_name='Price')
    st.session_state.strat_description = x.strategy_description()['msg']


def plot():
    base = alt.Chart(st.session_state.simple_payoff).properties(
        width=600,
        height=300
    )
    prices = base.encode(
        x="index",
        y="Price", color='ticker:N').mark_line()

    base_aggregated = alt.Chart(st.session_state.aggregated_payoff).properties(
        width=600,
        height=300
    )
    payoff_matu = base_aggregated.encode(
        x="index",
        y="Price", color='ticker:N').mark_line()

    st.altair_chart(prices)
    st.altair_chart(payoff_matu)


col1, col2, col3, col4 = st.columns(4)

with st.sidebar:
    with st.form("generate_graphs"):
        underlying_price = st.number_input('underlying_price', key='underlying_price', min_value=0.0, max_value=200.0,
                                           value=100.0)
        maturity = st.number_input('Maturity (Years)', key='maturity', min_value=0.0, max_value=5.0, value=0.25)
        interest_rate = st.number_input('Interest rate (%)', key='interest_rate', min_value=0.01, max_value=10.0,
                                        step=0.1)
        dividend_yield = st.number_input('Dividend Yield', key='dividend_yield', min_value=0)
        strategie = st.selectbox(
            'choose strat', strat, key='strat')
        submitted = st.form_submit_button("CALCULATE")

if submitted:
    with col1:
        load_data()
        plot()

    st.write(st.session_state.strat_description)