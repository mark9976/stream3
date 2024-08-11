import streamlit as st
from streamlit.components.v1 import html
from streamlit import session_state as ss

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'

st.set_page_config(initial_sidebar_state=ss.sidebar_state)

st.write("TEST")