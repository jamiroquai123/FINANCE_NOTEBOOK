import pandas as pd
import altair as alt
import streamlit as st


@st.cache
def load():
    df = pd.read_csv('tools/BS_db.csv')
    return df


input_C_P = alt.binding_select(options=['C', 'P'], name='tab_C/P')
selection_C_P = alt.selection_single(fields=['tab_C/P'], bind=input_C_P, init={'tab_C/P': 'C'})

slider_vol = alt.binding_range(min=1, max=100, step=1)
select_vol = alt.selection_single(name='Volatility (%)', fields=['tab_vol'],
                                  bind=slider_vol, init={'tab_vol': 30})

slider_matu = alt.binding_range(min=1, max=5, step=1)
select_matu = alt.selection_single(name='Matu (Years)', fields=['tab_maturity'],
                                   bind=slider_matu, init={'tab_maturity': 1})

base = alt.Chart(load()). \
    add_selection(select_vol, select_matu, selection_C_P). \
    transform_filter(select_vol). \
    transform_filter(select_matu). \
    transform_filter(selection_C_P). \
    properties(
    width=250,
    height=150
)
delta = base.encode(
    x="S",
    y="Delta",
    color=alt.value('red')).mark_line()

gamma = base.encode(
    x="S",
    y="Gamma",
    color=alt.value('blue')).mark_line()

theta = base.encode(
    x="S",
    y="Theta",
    color=alt.value('orange')).mark_line()

Lambda = base.encode(
    x="S",
    y="Lambda").mark_line()

vega = base.encode(
    x="S",
    y="Vega",
    color=alt.value('purple')).mark_line()

price = base.encode(
    x="S",
    y="Price",
    color=alt.value('yellow')).mark_line()

st.altair_chart(alt.concat(alt.vconcat(vega, theta, price, spacing=5),
                           alt.vconcat(delta, gamma, Lambda, spacing=5)))
