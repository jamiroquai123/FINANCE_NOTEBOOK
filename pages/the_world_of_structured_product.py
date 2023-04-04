import streamlit as st

chap = ['Introduction', 'The structured note', 'Libor Vs Treasury rate', 'Yield Curve', 'Time value of money',
        'The structured note', 'The sell side']

tabs = st.tabs(chap)
for tab_name, tab in zip(chap, tabs):
    if tab_name == 'Introduction':
        with tab:
            st.header(" **INTRODUCTION** ")

            st.markdown(
                'The business of eqd and hybrid structured product grew quicly. We describe how they came into existance.'
                'They can serve as diversification or yield enancement vehicle. Investment bank typically sell to retail client')

    elif tab_name == 'The structured note':
        with tab:
            st.header(" **'The structured note'** ")

            st.markdown(
                'strctured note = [non-risky asset (to provide protected capital) it can be zero coupon bond or bond that pay coupon during its life] +'
                ' [risky asset (to provide leverage potential) can be composed of options, the value of an option is always positive.'
                'Options enables holders to make additional profit with high leverage. The option price is non-linear]'
                'To summarize the structured note enables investor to receive high leverage potential while providing capital protection'
                '')
    elif tab_name == 'The sell side':
        with tab:
            st.header(" **'The sell side'** ")
            st.subheader('here we will focus on the role of people involved on the sell side of strctured product')
            st.title('Sales and marketing')
            st.markdown(
                'backtesting is a technique used by sells to show the potential benefit a client would have had '
                'stress test are used to show that even in a crash scenario the product react well')
