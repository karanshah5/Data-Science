import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
from eda import run_eda
from plots import show_plots

def main():
    st.title("Simple EDA App")
    st.subheader("EDA Web App with Streamlit ")
    st.markdown("""
        #### Description
        This is a simple Exploratory Data Analysis of 12 months worth of sales data built with Streamlit. 
        """)
    menu = ["EDA","Plots"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "EDA":
        run_eda()
        pass
    elif choice == "Plots":
        show_plots()


if __name__ == '__main__':
    main()










