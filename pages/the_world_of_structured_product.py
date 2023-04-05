import streamlit as st

chap = ['Introduction', 'The structured note', 'Libor Vs Treasury rate', 'Yield Curve', 'Time value of money',
        'The structured note', 'The sell side','Traders and structurers','The buy side']

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
    elif tab_name =='Traders and structurers':
        with tab:
            st.header(" **Traders and structurers** ")
            st.markdown(
                'The role of strctu varies from one institution to another but generally involves creating new strctures'
                'as well as pricing. It involves analysing the risks of suchs products. After a deal is sealed it goes '
                'to the trader portoflio who will be in charge to hedge the risks.'
                'Vanilla products are typically managed by volatility trader.'
                'The role of exo trader is to hedge. The more complex the product the more elaborate the risk')
            st.markdown('sales are interested in settling as many deals as possible to increase their commision')

    elif tab_name == 'The buy side':
        with tab:
            st.header(" **'The buy side'** ")
            st.subheader('to have meaning an exchange of cashflow involve more than one party. It can be classified '
                         'in two cattegory : retail and instit')
            st.title('retail')
            st.markdown(
                'it is usually asset management instit that buy structured products from investment bank and redistribute them '
                'to individual')