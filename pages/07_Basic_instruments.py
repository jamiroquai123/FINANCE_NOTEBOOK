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

st.markdown("For major ccy the interest rate paid on bond swap or future are plotted against their maturities, Those graphs are called Yield curves"
            "there is corporate curves that correspond to yields of bond issued by companies. Because their is higher credit risk"
            "thoses curves are usually higher and quoted in term of credit spread over libor. They are usually expressed as an annual rate "
            "to compare them easly. They are usually upward sloping with longer term rate higher than short term")


st.subheader("Time value of money")

st.markdown("An investor would prefer take possession of an amount of money today. In order to earn an interest of this money"
            "if we plan to pay me in one year, and r = 5 i could have earn 5 in this period of time. Therefore i discount it and concider that the present value is"
            "5 unit loosed ")

st.text("100 dollard future value expressed in today value if rate =5% per year is :")
st.latex('PV = FV * 1/(1 + i)^n')
st.latex('100/105')
st.latex('= 95.24')
st.text("n being the number of periods over witch we compound the interest")

st.markdown('Also, in this example it was an annual rate applied over a 1 year period. But we can think of coumponding as applying the rate to one period'
            'and reinvesting the result for another period and so on.'
            'So the presetn value at time 0 of a payment at time t in the future is given in term of future value')

st.latex('PV = FVe^-rt')

exo = st.expander(label='Exercice : If you make a deposit of 100$ today and interest rate are constant and equals to 10%'
                        'In the case of annual compounding how many years are needed for the value deposit to double to 200$')
with exo:
    st.latex("PV = FV * 1/(1 + i)^n")
    st.latex("n = ln(PV/FV) / ln(1 + i)")
    st.latex("n = ln(100/200) / ln(1 + 0,10)")
    st.markdown("7,27")



st.markdown("An investor would prefer take possession of an amount of money today. In order to earn an interest of this money")
