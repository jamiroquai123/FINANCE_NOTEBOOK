import streamlit as st

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
