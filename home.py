#*************************************************************
# Date: 11-AUG-2024
# Author: Mark Kaufmann
# File: home.py
#*************************************************************
# This is intended to be the home or landing page for the app.
# This is where the user will be redirected to the other functions.
#*************************************************************

#imports
import streamlit as st
from streamlit.components.v1 import html
from streamlit import session_state as ss

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'

st.set_page_config(initial_sidebar_state=ss.sidebar_state)





def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

st.title("ABARTA CAPA Database")

#layout setup
col1, col2, col3 = st.columns(3,gap="medium",vertical_alignment="center")

with col1:
    if st.button("Approved Documents"):
        nav_page('adocs')
with col2:
    if st.button("CAPA Records"):
        nav_page('records')
with col3:
    st.button("Placeholder")

st.camera_input("capture image")

