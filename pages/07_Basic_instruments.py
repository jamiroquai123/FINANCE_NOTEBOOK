import streamlit as st

st.header("1.1 INTRODUCTION")

st.markdown(
    "there is two type of financial instruments: exchange traded (listed products) or over the counter (OTC) that are privetly agreed :"
    "This include almost all swaps and exo derivatives")

st.markdown(
    'We first start by interest rate, the most important one is LIBOR, witch is the common floating rate for swap but '
    'also  used to compute the present value of future amount of money, We will also introduce discounting method which'
    'are important in the valuation of derivative')

st.markdown("In the topic of fixed income we will talk about essential debt instruments known as zero coupon."
            "Then we will talk about the basics of Equity and CCY market : features of stocks and factor impacting their future prices."
            "We will discuss how CCY cant be seen as a stock asset, forward and future")

st.markdown(
    "Finally we will talk about swap and how they are central in the OTC market (the most traded one being the interest rate swap)"
    "Then we will talk about cross ccy swap used to transform a loan in one ccy to another to finaly present total"
    " return swap wich replicate performance of assets such as equity or bonds")

st.header("1.2 INTEREST RATES")

st.markdown(
    "I.e represent the premium that has to be paid by the borrower or the lender. This amount of money depend of the "
    "credit risk (The risk induce by the incapacity of a debtor the reimbourse his debt) Therefore, the higher the credit risk "
    "the higher the interest rate charged by the lender")

st.subheader("Libor Vs Treasury rate")

st.markdown(
    "Among poopular rate, there is LIBOR (the london interbank offered rate) is the i.e at witch banks offer to lend fund "
    "to other banks in the interbank mkt. LIBOR will be a bit higher than the LIBID (london interbank bid rate) wich concist in "
    "the rate at wich banks accept deposit from other institution. "
    "Treasury rate (rates earned from bills or bonds issued by governements), depending on the governement,  "
    "these can be concidered as free risk rate as we suppose the governement won't fail")
st.markdown(
    "the diff between LIBOR and treasury rate is call the TED spread it can be seen as a measure of interbank lending "
    "liquidity LIBOR wich correspond to interbank lending compared to risk free rate of treasury bills is an indication of "
    "how willing banks are to lend money on each other"
    "LIBOR rates involves credit risk, wheareas treasury rates do not, Thus the TED spread serves as a measure of credit "
    "risk in the interbank market. The higher the TED spread correspond to higher perceived risk in lending and vice versa")

st.subheader("Yield Curve")

st.markdown(
    "For major ccy the interest rate paid on bond swap or future are plotted against their maturities, Those graphs are called Yield curves"
    "there is corporate curves that correspond to yields of bond issued by companies. Because their is higher credit risk"
    "thoses curves are usually higher and quoted in term of credit spread over libor. They are usually expressed as an annual rate "
    "to compare them easly. They are usually upward sloping with longer term rate higher than short term")

st.subheader("Time value of money")

st.markdown(
    "An investor would prefer take possession of an amount of money today. In order to earn an interest of this money"
    "if we plan to pay me in one year, and r = 5 i could have earn 5 in this period of time. Therefore i discount it and concider that the present value is"
    "5 unit loosed ")

st.text("100 dollard future value expressed in today value if rate =5% per year is :")
st.latex('PV = FV * 1/(1 + i)^n')
st.latex('100/105')
st.latex('= 95.24')
st.text("n being the number of periods over witch we compound the interest")

st.markdown(
    'Also, in this example it was an annual rate applied over a 1 year period. But we can think of coumponding as applying the rate to one period'
    'and reinvesting the result for another period and so on.'
    'So the presetn value at time 0 of a payment at time t in the future is given in term of future value')

st.latex('PV = FVe^-rt')

exo = st.expander(
    label='Exercice : If you make a deposit of 100$ today and interest rate are constant and equals to 10%'
          'In the case of annual compounding how many years are needed for the value deposit to double to 200$')
with exo:
    st.latex("PV = FV * 1/(1 + i)^n")
    st.latex("n = ln(PV/FV) / ln(1 + i)")
    st.latex("n = ln(100/200) / ln(1 + 0,10)")
    st.markdown("7,27")

st.markdown(
    "An investor would prefer take possession of an amount of money today. In order to earn an interest of this money")
st.subheader("Bonds")

st.markdown(
    'The bond is a debt securitie issued by governement and companies. In exchange of the funds, the holder is entilted to receive coupons paid periodicly'
    'as well as the return of initial investment. The coupon can also be linked to an index, we then talk about floating rate note'
    'The market price of a bond is equal to the sum of the present value of expecte cashflow')

st.text('t the variation rate and C the value that are still to be paid at coupon dates')

st.latex(r'Bond(t,T) = \[ \sum_{n=1}^{n} CiB(t,ti)\]')
st.text('witch is equal to')
st.latex(r'Bond(t,T) = \[ \sum_{n=1}^{n} Cie^{-r(t,ti) * (ti-t)}\]')
st.text('expressed in term of yield to maturity')
st.latex(r'Bond(t,T) = \[ \sum_{n=1}^{n} Cie^{-y(ti-t)}\]')

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

st.subheader("Zero coupon Bonds")

st.markdown(
    'Zero coupon bonds are debpt investments when the lender receives back a principal amount (also called notional) '
    'plus interest only at matu. No coupon are paid during the life of the product.'
    'The interst is deduced upfront and reflected in the price, wich means that is price is lower than 100% of the notional'
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
