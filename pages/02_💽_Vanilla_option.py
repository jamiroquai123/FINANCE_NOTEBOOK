import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout="centered")
st.title("Vanilla Options")
st.header('General feature of options')
st.text("Contrat entre deux parties, qui donne aux acheteurs un droit mais pas une obligation \n"
        "d'acheter ou de vendre un actif a un certain prix")

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
