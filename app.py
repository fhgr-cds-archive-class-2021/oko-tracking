import streamlit as st
from streamlit_option_menu import option_menu
from src.overview.page import page as overview_page
from src.spot_a_difference.page import page as spot_difference_page
from src.metro.page import page as metro_page

st.set_page_config(page_title="Oko Tracking Group", page_icon="👁")

with st.sidebar:
    choose = option_menu("Menu", ["Overview", "Spot-a-difference", "Metro"],
                         icons=["book", "stopwatch", "bezier2", "magic"],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "transparent"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#036314"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )


if choose == "Overview":
    overview_page()
elif choose == "Spot-a-difference":
    spot_difference_page()
elif choose == "Metro":
    metro_page()