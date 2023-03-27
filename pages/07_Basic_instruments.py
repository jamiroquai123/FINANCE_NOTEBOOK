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
