import streamlit as st

chap = ['Introduction', 'Interest Rates', 'Libor Vs Treasury rate', 'Yield Curve', 'Time value of money','Bonds',"Zero coupon Bonds"]

tabs = st.tabs(chap)
for tab_name, tab in zip(chap, tabs):
    if tab_name == 'Introduction':
        with tab:
            st.header(" **INTRODUCTION** ")

            st.markdown(
                'There is **:red[two]** type of financial instruments: - :red[exchange traded] (**listed products**)'
                " or  : - :red[over the counter] **(OTC)** that are privetly agreed : This include almost all swaps and exo derivatives")

            st.markdown(
                'We first start by interest rate, the most important one is **LIBOR**, witch is :red[the common floating rate for SWAP] but '
                'also used to compute the present value of future amount of money. We will also introduce :red[discounting method] which'
                ' are important in the valuation of derivative')

            st.markdown(
                "In the topic of fixed income we will talk about essential debt instruments known as :red[zero coupon]."
                "Then we will talk about the basics of Equity and CCY market : features of stocks and factor impacting their future prices.")

            st.markdown(
                "Finally we will talk about SWAP and how they are central in the OTC market (the most traded one being the **interest rate SWAP**)"
                "Then we will talk about cross ccy swap used to transform a loan in one ccy to another to finaly present total"
                " return swap wich replicate performance of assets such as equity or bonds")
    elif tab_name == 'Interest Rates':
        with tab:
            st.header(" **INTEREST RATES** ")
            st.markdown(
                "Ie represent the :red[premium that has to be paid by the borrower or the lender]. This amount of money depend of the "
                "credit risk (The risk induced by the incapacity of a debtor the reimbourse his debt) Therefore, :red[the higher the credit risk "
                "the higher the interest rate charged by the lender]")
    elif tab_name == 'Libor Vs Treasury rate':
        with tab:
            st.subheader("Libor Vs Treasury rate")
            st.markdown(
                "Among popular rates, there is **LIBOR** (_the london interbank offered rate_) is the ie at witch banks offer to lend funds "
                "to other banks in the interbank mkt. **LIBOR** will be a bit higher than the **LIBID** (london interbank bid rate) wich concist in "
                "**the rate at wich banks accept deposit from other institution**. "
                "Treasury rate (rates earned from bills or bonds issued by governements), depending on the governement,  "
                "these can be concidered as free risk rate as we suppose the governement won't fail")
            st.markdown(
                "The diff between LIBOR and treasury rate is call the TED spread it can be seen as a measure of interbank lending "
                "liquidity LIBOR wich correspond to interbank lending compared to risk free rate of treasury bills is an indication of "
                "how willing banks are to lend money on each other"
                "LIBOR rates involves credit risk, wheareas treasury rates do not, Thus the TED spread serves as a measure of credit "
                "risk in the interbank market. The higher the TED spread correspond to higher perceived risk in lending and vice versa")
    elif tab_name == 'Yield Curve':
        with tab:
            st.subheader("Yield Curve")
            st.markdown(
                "For major ccy the interest rate paid on bond swap or future are plotted against their maturities, Those graphs are called Yield curves"
                "there is corporate curves that correspond to yields of bond issued by companies. Because their is higher credit risk"
                "thoses curves are usually higher and quoted in term of credit spread over libor. They are usually expressed as an annual rate "
                "to compare them easly. They are usually upward sloping with longer term rate higher than short term")
    elif tab_name == 'Time value of money':
        with tab:
            st.subheader("Time value of money")
            st.markdown(
                "An investor would prefer take possession of an amount of money today. In order to earn an interest on this money"
                "if we plan to pay me in one year, and r = 5 I could have earn 5 in this period of time. Therefore i "
                "discount it and concider that the present value is 5 unit discounted")

            st.text("100 dollar future value expressed in today value if rate = 5% per year is :")
            st.text("with n being the number of periods over witch we compound the interest")
            st.latex('PV = FV * 1/(1 + i)^n')
            st.latex('= 100/1,05')
            st.latex('= 95.24')

            st.markdown(
                'Also, in this example it was an annual rate applied over a 1 year period.'
                'But we can think of coumponding as applying the rate to one period and reinvesting the result for another period and so on.'
                'So the present value at time 0 of a payment at time t in the future is given in term of future value')

            st.latex('PV = FVe^-rt')
            st.markdown(
                'Exercice:If you make a deposit of 100$ today and interest rate are constant and equals to 10%'
                'In the case of annual compounding how many years are needed for the value deposit to double to 200$')
            exo = st.expander(label='Solution')
            with exo:
                st.latex("PV = FV * 1/(1 + i)^n")
                st.latex("n = ln(PV/FV) / ln(1 + i)")
                st.latex("n = ln(100/200) / ln(1 + 0,10)")
                st.latex("n = 7,27")
    elif tab_name == 'Bonds':
        with tab:
            st.subheader("Bonds")

            st.markdown(
                'The bond is a debt securitie issued by governement and companies. In exchange of the funds, the holder '
                'is entilted to receive coupons paid periodicly as well as the return of initial investment. '
                'The coupon can also be linked to an index, we then talk about floating rate note '
                'The market price of a bond is equal to the sum of the present value of expected cashflow')

            st.text('t the variation rate and C the value that are still to be paid at coupon dates')
            st.latex('Bond(t,T) = sum{n=1}^{n} CiB(t ,ti)\]')
            st.text('witch is equal to')
            st.latex('Bond(t,T) = [ \sum_{n=1}^{n} Cie^{-r(t,ti) * (ti-t)}\]')
            st.text('expressed in term of yield to maturity')
            st.latex('Bond(t,T) = [ \sum_{n=1}^{n} Cie^{-y(ti-t)}\]')

            st.markdown(
                "The price of a bond may include the interest rate that has accrued since the last coupon date"
                "The price including accrued interest is known as dirty price and correspond to the fair value of the bond"
                "Quoted bond display clean prices witch doesn't include accrued interest")
            st.latex('Clean price = Dirty price - accrued interest')

            st.markdown(
                'bonds are concidered to be safer instruments than stocks, Bonds can pay higher interest compare to stocks dividend'
                'Also bonds suffer from less liquidity issues than stocks'
                'Nonetheless bond are not risk free, because they are a direct function of interest rate. A rise of the market interest'
                'decrease values of bonds. If the interest rate used to discount the coupon goes up their present value goes down'
                'Also Bond price depend on the credit rating of the issuer if the risk of credit increase the value of bond decrease. '
                'Therefore credit risk increase volatility of bond prices. In the case of callable bonds, the bond can be called'
                'ie bought back by the issuer. Buying a callable bond is equivalent to buying a bond and selling an american call option on this bond.'
                'When interest rate go down, price of bond increase and issuer tend to exercice their call and buy back the bond')
    elif tab_name == 'Zero coupon Bonds':
        with tab:
            st.subheader("Zero coupon Bonds")
            st.markdown(
                'Zero coupon bonds are debpt investments when the lender receives back a principal amount (also called notional) '
                'plus interest only at matu. No coupon are paid during the life of the product.'
                'The interest is deduced upfront and reflected in the price, wich means that is price is lower than 100% of the notional'
                'it is better in a medium term liquidity perspective because no payment have to be made in the meantime'
                'The price of such an bond is equal to the present value of the par value')
            st.latex('Linear : interest is proportional to the lengh of the loan')
            st.latex('B(t,T) = 1/1+ r(t,T) * (T-t)')
            st.latex('Actuarial : interest is compounded periodically')
            st.latex('B(t,T) = 1/1+ r(t,T))^{(T-t)}')
            st.latex('Continuous : interest is compounded continuously')
            st.latex('B(t,T) =e^{-r(t,T) x (T-t)')

st.header("Equities and currency")

st.subheader('Stocks')

st.markdown(
    'often companies need cash, and choose to raise it by issuing equity, a share of stock entitle the ownership '
    'of someone to a corporation, it usually pay dividend, it can be seen as a part of company profit distributed.'
    'Therefore the price of a stock usually drop by the div amount before the ex-div date.'
    'if someone beleive the stock will drop he can enter into a repurshase agreement or repo.'
    'Its a transaction in wwitch an investor borrow the stock and agree to give it back at a certain date.'
    'You can then borrow the stock sell it and buy it cheaper later on.'
    'Liquidity is correlated to the stock price. expensive stock are not affordable to anyone and thus suffer from liquidity problem'
    'corporate action need to be taken account as they can have a large impact on a stock price.'
    'Stock split and reverse stock split are respectivly used to increase or decrease the number of shares.'
    'The forward price of a stock is defined as the fair value of the stock. It can be seen as the spot price plus the cost of carrying it'
    'if spot = 50 and rate is % the forward price is 50e^0,5 * 6/12. As the dividend increase the profit it reduce the cost '
    'of carrying a stock and so does the repo. Therefore thos parameters decrease the forward price.')

st.latex('F0(T) = S0 * e ^{r-q-b)*T}')

st.subheader('Foreign Exchange')

st.markdown('a ccy is a financial instrument that can be traded in term of spot or forward contracts'
            'FX future are always quoted in term of dollar per unit of foraign ccy. if the spot exchange rate between GBP and USD '
            'is equal to two this mean 1GBP = 2 Dollar')

st.latex('F0(T) = S0 * e ^{rd-rf)*T}')

st.markdown(
    "if a trader want to exchange ccy A for ccy B but cannot find a quote price he can use the available excahnge rates he would then"
    "compute the cros rate :")

st.latex('A/B = A/C * C/B')

st.subheader('Indices')

st.markdown(
    'Index is composed of basket of a stock and provide a way to measure perf of a sector. American SNP Japanese nikkei german dax british ftset '
    'Hongkong hangseng =')

st.subheader('Exchange traded fund')

st.markdown('Etf hold assets such as stock or bond and try to replicate the price of another assets'
            'Diversification reduce risk, so many investor are interested in basket of assets or indices. However'
            'it is impractical to buy indices because of the need to rebalance with the index. Therefore etf can be a great solution.'
            '')

st.subheader('Forward contracts')

st.markdown(
    'The forward is an agreement to buy or cell at a certain price at a specified point in the future. It is OTC (over the counter)'
    'The price agreed to buy or sell is called the strike price.'
    'One could use the forward for two reason'
    '(1) the price will increase'
    '(2) the value of the asset will appreciate and enter into forward to avoid this scenario.'
    '(3) additionnaly it can serve as hedging instrument'
    'Generally strike price is equal to the fair value of the forward price at the issue date. This implied that '
    'usually forward have zero mark to market value'
    'To price the forward contract one should discount the diff between the forward price and the strike price')

st.latex('Forward(T) = (Ft(T) - K) * e^{-r*(T-t)}')

exo_forward = st.expander(
    label='Exercice : John beleive the stock price of Vodaphone will appreaciate'
          'Vodaphone is worth £80 and the 1-year LIBOR rate r is 6%, the div yield is equal to 2% and borrowing cost are null'
          'He enter into a 1 year forward contract allowing him to buy 1000 shares in one year at K=£82.'
          'After one year Vodaphone spot is £86 Did john realized a profit.')
with exo_forward:
    st.latex('Ft(T) = 80^{0,06 - -0,02} = 83')
    st.latex('Forward(T) = (Ft(T) - 82) * e^{-0,06}')
    st.latex('Forward(T) = (83 - 82) * e^{-0,06} = £1224')
    st.latex("johns profit = 1000 * (86 - 82) = £4000")
    st.markdown("John makes 2776 profit")

st.subheader('Futures')

st.markdown('A future contract is an obligation to sell or buy at a certain price in the future,'
            'much like a forward except they are trade on the regular market.'
            'They are a great option to hedge an equity position or to speculate.'
            'They are a safer investment than forward because the risk of counterparty is limited by the clearing house act '
            'that provides margin calls.'
            'They are market to market on a daily basis to the new future prices.'
            'The quoted price of the future contract is the future price itself. The fair value of a future is equal to the cash price'
            'of the asset (The spot value of the asset) plus the cost of carry '
            'When a future contracts trade above its fair value, a cash and carry arbitrage opportunity arise.'
            'One would immediatly buy the asset at spot price to hold it until the settlement date and at the same time'
            'sell the future at the market future price. At delivery date he has done a profit equal to the diff'
            'between future price and the fair value.'
            'The opposite occurs when the future is trading below the fair value. One could short sell the asset and take a long position '
            'on the future')

st.header('SWAPS')
st.subheader('Interest rate swap')

st.markdown('A specific example is a plain vanilla swap, when two counterparty swap a fixed rate and the floating rate'
            'Payment are netted, because all cashflow are in the same ccy. For instance a payment of 5% fixed and receipt of '
            '4% floating will result in a 1% payment'
            'The payer of a swap is the personn who agrees to pay the fixed rate( and receive the floating rate) The Payer is concern that'
            'the floating rate will increase.'
            'The receiver is th personn who aggrees to receive the fixed rate and pay the floating rate on an IRS. He expect'
            'interest rate to fall and is refered as being short the swap.'
            'IRS are usefull when it come to borrow money. A compagny may borrow money at fixed rate if they though '
            'ie are going to increase and the opposite if they think ie will go down')

st.markdown('For instance a 5year and 3month borrowing facility.'
            '5 years are splited into 3 month period, at the beggining of each 3 month period the 3month libor rate is set'
            'and aplied to the loan. At the end of each period interest are paid and the new libor rate is set.'
            'A company with such a facility may approach another institution and arange an IRS. The company would aggree'
            'to pay LIBOR at the end of 3 month periods in exchange for interest payment.'
            'A basis swap is a particular type of IRS where floating rate is swapped for a different floating rate.'
            'To compute the value of a swap, one should calculate the net present value (NPV) of all future cashflows'
            'Wich is equal to the present value from receiving leg minus the present value from the paying leg.'
            'Initially it is set up in a way that its value is null. Meaning that someone can enter a swap at zero cost.')

exo_swap = st.expander(
    label='Exercice : lets E denote the 3month EURIBOR rate. Consider an interest swap contract where Party A pays E to party B '
          'and party B pays 24% -3 x E to party A.'
          'Let L denote the notional of this swap. Can you express the deal in simpler terms ')
with exo_swap:
    st.markdown('Party A pays E and receive 24% -3E')
    st.markdown('Then party receive 24% - 4E ==  4 x (8%-E)')
    st.markdown(
        "This contract is then equivalent to an Interest rate swap Where A (the receiver) receive 8% from B(the payer) and pays E to "
        "party B"
        "The notional is equal to 4 x N")

st.subheader('Cross currency swap')
st.subheader('Total return Swap (TRS)')
st.markdown('it is a swap aggreement in witch a party pays fixed or float interest and receive total return of an asset'
            'total return is the capital gain or loss from the asset in addition to any interestor div received during the life'
            'of the swap. It enables both party to gain exposure to a specific asset without having to pays additional costs')

st.subheader('Asset swap')
st.markdown(
    'An asset swap is otc agreement in which the payment of one leg are funded by a specific asset, it can be a bond for instance$'
    'where the coupons are used as payement on one leg of the swap, but generally the bond or the asset underlying this swap does not exchange hand')

st.subheader('dividend swap')
st.markdown(
    'its an otc on an index or a stock and involve two counter parties who exchanges cashflow based on the div paid.')
