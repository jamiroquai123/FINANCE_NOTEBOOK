import pandas as pd

"""st.session_state.strike_price = 100
st.session_state.maturity = 0.25
st.session_state.interest_rate = 0.1
st.session_state.volatility = 30
st.session_state.dividend_yield = 0
submitted = st.form_submit_button("CALCULATE")"""

"""@st.cache
def load():
    super_dict = list()
    a = [[i for i in range(1, 101, 1)], [i for i in range(1, 6, 1)],['C','P']]
    goumber = list(itertools.product(*a))
    for i in goumber:
        st.session_state.volatility = i[0]
        st.session_state.maturity = i[1]
        st.session_state.call_or_put = i[2]
        x = Plot()
        x.computeoption()
        for delta, gamma, theta, vega, Lambda, Price, s in \
                zip([o.delta() for o in x.option], [o.gamma() for o in x.option], [o.theta() for o in x.option],
                    [o.vega() for o in x.option], [o.Lambda() for o in x.option], [o.price() for o in x.option],
                    x.Sset):
            super_dict.append({
                "tab_C/P": i[2],
                "tab_vol": i[0],
                "tab_maturity": i[1],
                "Delta": delta,
                "Gamma": gamma,
                "Theta": theta,
                "Vega": vega,
                "Lambda": Lambda,
                "Price": Price,
                "S": s})
    return super_dict
"""
df = pd.read_csv('BS_db.csv').rename(columns={"Unnamed: 0":'tab_C/P'})
print()