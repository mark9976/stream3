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

def get_file_names_from_snowflake(conn, table_name):
    cursor = conn.cursor()
    query = f"SELECT file_name FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    
    # Flatten the result list
    file_names = [row[0] for row in result]
    return file_names

def get_approval_date_from_snowflake(conn, table_name):
    cursor = conn.cursor()
    query = f"SELECT date FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    
    # Flatten the result list
    approval_dates = [row[0] for row in result]
    return approval_dates


conn = st.connection("snowflake")


col1, col2, col3 = st.columns(3,gap='medium', vertical_alignment='center')
files = ''
dates = ''
with col1:
    st.button("Create/Upload new Approved document")
    #list the approved docs
    files = get_file_names_from_snowflake(conn, 'MKTEST.PDFTESTER.pdf_files')
    dates = get_approval_date_from_snowflake(conn, 'MKTEST.PDFTESTER.pdf_files')
    
with col2:
    if st.button("Preview and existing Approved document"):
    #jump to preview page
    #get the listing of all of the current documents
        nav_page('preview')
with col3:
    st.button("Download document")


st.header("Listing of Approved Documents")
st.table({'File Name': files, 'Approval Dates':dates})

