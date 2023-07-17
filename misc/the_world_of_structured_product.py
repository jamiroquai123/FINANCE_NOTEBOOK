import streamlit as st

chap = ['Introduction', 'The structured note', 'Libor Vs Treasury rate', 'Yield Curve', 'Time value of money',
        'The structured note', 'The sell side', 'Traders and structurers', 'The buy side', 'Bullish vs bearish',
        'credit risk and collateralized line']

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
    elif tab_name == 'Traders and structurers':
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

    elif tab_name == 'Bullish vs bearish':
        with tab:
            st.header(" **'Bullish vs bearish'** ")
            st.subheader('Bullshish investor believe the market will go up, bearish expect the market to go down,'
                         'in growth period investor = bullish in recession period investor = bearish')
            st.title('short vs long')
            st.markdown(
                'someone long an asset want its value to appreciate, if the opposite this investor is said to be short'
                'For instance the holder of a floating bond is long the bond. but is also short interest rate.'
                'Capital protected products are popular since they allow a return at matu at least equal to the original'
                'investment plus a leverage opportunity.'
                'Yield enhancement product offer above the market returns as long as an event didnt occured'
                'Different type of products offer different type of payement depending on the way client wants to be paid')

            st.markdown('Income structured products offer periodic coupon payments$'
                        'in the case of capital guaranteed income products, the non risky part paying fixed coupon is composed of bonds paying periodic fixed coupon'
                        'and 100% of the notional at maturity')

            st.markdown(
                'a growth products produce a return at matu based on the performance of an underlying with no coupon payment'
                'during its life')
    elif tab_name == 'credit risk and collateralized line':
        with tab:
            st.header(" collateralized line")
            st.subheader('collateralized lines are those who does not involve counterparty risk'
                         'For SWAPS the way to avoid problem is to structure the swap along colateralized lines.'
                         'This involve computing the value of the swap and setting aside the equivalent amount of collateral')
            st.markdown(
                'when building a structured note, bonds of the bank with lower credit rating cost less and thus there is more'
                'money to put into the risky part of the note')

            st.markdown('Income structured products offer periodic coupon payments$'
                        'in the case of capital guaranteed income products, the non risky part paying fixed coupon is composed of bonds paying periodic fixed coupon'
                        'and 100% of the notional at maturity')

            st.markdown(
                'a growth products produce a return at matu based on the performance of an underlying with no coupon payment'
                'during its life')
    elif tab_name == 'THE MARKET':
        with tab:
            st.header("THE MARKET")
            st.subheader('issuing a structured product')
            st.markdown(
                'Investment bank can raise capital through issuing structured products at specific price expressed in '
                'percentage of notional size')
            st.subheader('EXAMPLE OF AN EQUITY LINKED NOTE')
            st.markdown(
                    'An equity linked note (ELS) is a simple structured products that makes a single payment to the specific '
                    'investor at matu of a percentage of capital plus participation on the positive perf.'
                    'it is composed of a zero coupon bond delivering a guaranteed notional amount at matu and an european call option on the '
                    'underlying asset'
                    'ELNvalue = ZCprice + Callprice + P&L ')
