import pandas as pd
import streamlit as st
from tools.Delta_visu import Plot
import altair as alt


def load_data():
    st.session_state.plot = True
    x = Plot()
    x.computeoption()
    st.session_state.df = pd.DataFrame({"Delta": [o.delta() for o in x.option],
                                        "Gamma": [o.gamma() for o in x.option],
                                        "Theta": [o.theta() for o in x.option],
                                        "Vega": [o.vega() for o in x.option],
                                        "Lambda": [o.Lambda() for o in x.option],
                                        "Price": [o.price() for o in x.option],
                                        "S": x.Sset})


def plot_data():
    base = alt.Chart(st.session_state.df).properties(
        width=300,
        height=150
    )
    base_cache = alt.Chart(st.session_state.cache).properties(
        width=300,
        height=150
    )
    prices = base.encode(
        x="S",
        y="Price", color=alt.value('red')).mark_line()

    pricexrule = (
        base.encode(
            x="S",
            y="Price").mark_line()
        .mark_rule(color="cyan", strokeWidth=1)
        .encode(x=alt.datum(100))
    )
    pricexcache = base_cache.encode(
        x="S",
        y="Price").mark_line(opacity=0.4)

    lambdas = base.encode(
        x="S:Q",
        y="Lambda:Q", color=alt.value('green')).mark_line()

    lambdaxrule = (
        base.encode(
            x="S:Q",
            y="Lambda:Q").mark_line()
        .mark_rule(color="cyan", strokeWidth=1)
        .encode(x=alt.datum(100))
    )
    lambdaxcache = base_cache.encode(
        x="S:Q",
        y="Lambda:Q").mark_line(opacity=0.4)

    vega = base.encode(
        x="S",
        y="Vega", color=alt.value('orange')).mark_line()

    vegaxrule = (
        base.encode(
            x="S",
            y="Vega").mark_line()
        .mark_rule(color="cyan", strokeWidth=1)
        .encode(x=alt.datum(100))
    )
    vegaxcache = base_cache.encode(
        x="S",
        y="Vega").mark_line(opacity=0.4)

    theta = base.encode(
        x="S",
        y="Theta", color=alt.value('yellow')).mark_line()
    thetaxrule = (
        base.encode(
            x="S",
            y="Theta").mark_line()
        .mark_rule(color="cyan", strokeWidth=1)
        .encode(x=alt.datum(100))
    )
    thetaxcache = base_cache.encode(
        x="S",
        y="Theta").mark_line(opacity=0.4)
    delta = base.encode(
        x="S",
        y="Delta", color=alt.value('purple')).mark_line()
    deltaxrule = (
        base.encode(
            x="S",
            y="Delta").mark_line()
        .mark_rule(color="cyan", strokeWidth=1)
        .encode(x=alt.datum(100))
    )
    deltaxcache = base_cache.encode(
        x="S",
        y="Delta").mark_line(opacity=0.4)
    gamma = base.encode(
        x="S",
        y="Gamma", color=alt.value('violet')).mark_line()
    gammaxrule = (
        base.encode(
            x="S",
            y="Gamma").mark_line()
        .mark_rule(color="cyan", strokeWidth=1)
        .encode(x=alt.datum(100))
    )
    gammaxcache = base_cache.encode(
        x="S",
        y="Gamma").mark_line(opacity=0.4)
    st.altair_chart(
        alt.concat(
            alt.vconcat(vega + vegaxrule + vegaxcache, theta + thetaxrule + thetaxcache,
                        delta + deltaxrule + deltaxcache),
            alt.vconcat(lambdas + lambdaxrule, prices + pricexrule + pricexcache,
                        gamma + gammaxrule + gammaxcache)))


with st.sidebar:
    with st.form("generate_graphs"):
        call_or_put = st.selectbox('Call or Put (C/P)', ['C', 'P'], key='call_or_put')
        strike_price = st.number_input('Strike Price', key='strike_price', min_value=2, value=100)
        maturity = st.number_input('Maturity (Years)', key='maturity', min_value=0.0, max_value=5.0, value=0.25)
        interest_rate = st.number_input('Interest rate (%)', key='interest_rate', min_value=0.01, max_value=10.0,
                                        step=0.1)
        volatility = st.number_input('Volatility (%)', key='volatility', min_value=1, max_value=100, value=30)
        dividend_yield = st.number_input('Dividend Yield', key='dividend_yield', min_value=0)
        submitted = st.form_submit_button("CALCULATE")

if "plot" not in st.session_state:
    st.session_state.plot = False

if submitted:
    if 'volatility_twister' in st.session_state: del st.session_state['volatility_twister']
    if 'rate_twister' in st.session_state: del st.session_state['rate_twister']
    if 'maturity_twister' in st.session_state: del st.session_state['maturity_twister']
    load_data()

if st.session_state.plot:
    if 'df' not in st.session_state:
        load_data()
    st.session_state.cache = st.session_state.df
    with st.expander("⚙"):
        vol = st.slider('vol %', 1, 100, on_change=load_data(), key='volatility_twister',
                        value=st.session_state.volatility)
        rate = st.slider('rate %', 0.01, 10.0, on_change=load_data(), key='rate_twister',
                         value=st.session_state.interest_rate)
        matu = st.slider('matu year', 0.01, 5.0, on_change=load_data(), key='maturity_twister',
                         value=st.session_state.maturity)
    plot_data()
