import pandas as pd
import streamlit as st
from tools.Delta_visu import Plot

@st.cache
def load_option():
    data = Plot()
    data.computeoption()
    return data

def spin():
    display_call()

def display_call():
    col1,padding, col2 = st.columns((100,2, 200))
    padding.latex(
        r"""\mathrm C(\mathrm S,\mathrm t)= \mathrm N(\mathrm d_1)\mathrm S - \mathrm N(\mathrm d_2) \mathrm K \mathrm e^{-rt}""")
    st.write("#")
    x = Plot()
    x.computeoption()
    #"PRICES AND LAMBDA"
    col1,padding, col2 = st.columns((200,2,200))
    col1.line_chart(
        data=pd.DataFrame.from_dict({"Prices": [o.price() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset}),
        x=f"Underlying S strike={st.session_state.strike_price}", y="Prices",height=200)
    col2.line_chart(
        data={"Lambda": [o.Lambda() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset},
        x=f"Underlying S strike={st.session_state.strike_price}", y="Lambda", height=200)

    #"DELTA AND GAMMA"
    col1, padding, col2 = st.columns((200, 2, 200))
    col1.line_chart(
        data=pd.DataFrame.from_dict(
            {"Delta": [o.delta() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset}),
        x=f"Underlying S strike={st.session_state.strike_price}", y="Delta", height=200)
    col2.line_chart(
        data={"Gamma": [o.gamma() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset},
        x=f"Underlying S strike={st.session_state.strike_price}", y="Gamma", height=200)

    #"THETA AND VEGGA"
    col1, padding, col2 = st.columns((200, 2, 200))
    col1.line_chart(
        data=pd.DataFrame.from_dict(
            {"Theta": [o.theta() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset}),
        x=f"Underlying S strike={st.session_state.strike_price}", y="Theta", height=200)
    col2.line_chart(
        data={"Vega": [o.vega() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset},
        x=f"Underlying S strike={st.session_state.strike_price}", y="Vega", height=200)

def display_put():
    col1, padding, col2 = st.columns((100, 2, 200))
    padding.latex(r"delta(put)=\frac{\partial p}{\partial S}=e^{-q(T-t)}(N(d1)-1)")
    st.write("#")
    x = Plot()
    x.computeoption()

    # "PRICES AND LAMBDA"
    col1, padding, col2 = st.columns((200, 2, 200))
    col1.line_chart(
        data=pd.DataFrame.from_dict(
            {"Prices": [o.price() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset}),
        x=f"Underlying S strike={st.session_state.strike_price}", y="Prices", height=200)
    col2.line_chart(
        data={"Lambda": [o.Lambda() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset},
        x=f"Underlying S strike={st.session_state.strike_price}", y="Lambda", height=200)

    # "DELTA AND GAMMA"
    col1, padding, col2 = st.columns((200, 2, 200))
    col1.line_chart(
        data=pd.DataFrame.from_dict(
            {"Delta": [o.delta() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset}),
        x=f"Underlying S strike={st.session_state.strike_price}", y="Delta", height=200)
    col2.line_chart(
        data={"Gamma": [o.gamma() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset},
        x=f"Underlying S strike={st.session_state.strike_price}", y="Gamma", height=200)

    # "THETA AND VEGGA"
    col1, padding, col2 = st.columns((200, 2, 200))
    col1.line_chart(
        data=pd.DataFrame.from_dict(
            {"Theta": [o.theta() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset}),
        x=f"Underlying S strike={st.session_state.strike_price}", y="Theta", height=200)
    col2.line_chart(
        data={"Vega": [o.vega() for o in x.option], f"Underlying S strike={st.session_state.strike_price}": x.Sset},
        x=f"Underlying S strike={st.session_state.strike_price}", y="Vega", height=200)

with st.sidebar:
    with st.form("generate_graphs"):
        call_or_put = st.selectbox('Call or Put (C/P)', ['C', 'P'], key='call_or_put')
        strike_price = st.number_input('Strike Price', key='strike_price', min_value=2,value=100)
        maturity = st.number_input('Maturity (Years)', key='maturity', min_value=0.0, max_value=5.0,value=0.25)
        interest_rate = st.number_input('Interest rate (%)', key='interest_rate', min_value=0.01, max_value=10.0,
                                        step=0.1)
        volatility = st.number_input('Volatility (%)', key='volatility', min_value=1, max_value=100,value=30)
        dividend_yield = st.number_input('Dividend Yield', key='dividend_yield', min_value=0)
        submitted = st.form_submit_button("CALCULATE")

if 'C' in st.session_state.call_or_put and submitted:
    display_call()
elif 'P' in st.session_state.call_or_put and submitted:
    display_put()
