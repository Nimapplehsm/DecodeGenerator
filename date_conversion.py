# import streamlit as st

# def render_date_conversion_page():
#     st.title("Informatica Date Conversion")

#     st.subheader("Input Details")
    
#     # Input date string
#     input_string = st.text_input("Enter the date string to convert:", key="input_string")

#     # Input date format
#     input_format = st.text_input("Specify the input format (e.g., YYYY-MM-DD, DD-MON-YYYY):", key="input_format")
    
#     # Conversion type: TO_DATE or TO_CHAR
#     conversion_type = st.radio("Select Conversion Type:", ["TO_DATE", "TO_CHAR"], key="conversion_type")

#     # Output format (only for TO_CHAR)
#     output_format = st.text_input("Specify the output format (e.g., DD-MON-YYYY, MM/DD/YYYY):", key="output_format") \
#         if conversion_type == "TO_CHAR" else None

#     st.subheader("Generated SQL Function")
    
#     # Generate the SQL function based on user inputs
#     if st.button("Generate"):
#         if conversion_type == "TO_DATE":
#             if input_string and input_format:
#                 sql_function = f"TO_DATE('{input_string}', '{input_format}')"
#                 st.code(sql_function, language="sql")
#             else:
#                 st.error("Both input string and format are required for TO_DATE.")
#         elif conversion_type == "TO_CHAR":
#             if input_string and input_format and output_format:
#                 sql_function = f"TO_CHAR(TO_DATE('{input_string}', '{input_format}'), '{output_format}')"
#                 st.code(sql_function, language="sql")
#             else:
#                 st.error("Input string, input format, and output format are required for TO_CHAR.")

#     # Navigation button to go back to main input page
#     if st.button("Back to Main Page"):
#         st.session_state.page = "input"  # Set the session state to return to the main input page
#         st.rerun()  # Reload the app

import streamlit as st
from db_elements import db_elements  # Import the db_elements list
from OutputFormats import output_formats,input_formats

def render_date_conversion_page():
    st.title("Date Conversion")

    st.subheader("Input Details")
    
    # Drop-down for DB Element selection from the provided db_elements list
    input_string = st.selectbox("Select the DB element to convert:", db_elements, key="input_string")

    # Drop-down for input format selection
    #input_formats = ["YYYY-MM-DD", "DD-MON-YYYY", "MM/DD/YYYY", "YYYY/MM/DD"]  # Predefined formats
    input_format = st.selectbox("Select the input format:", input_formats, key="input_format")
    
    # Conversion type: TO_DATE or TO_CHAR
    conversion_type = st.radio("Select Conversion Type:", ["TO_DATE", "TO_CHAR"], key="conversion_type")

    # Drop-down for output format selection (only for TO_CHAR)
    #output_formats = ["DD-MON-YYYY", "MM/DD/YYYY", "YYYY/MM/DD", "YYYY-MM-DD","MM/DD/YY","MON DD YYYY HH12:MI:SSAM","MM/DD/RR","MONTH","DD-MON-YYYY","YYYY-MON-DD","DD-MON-YYYY","HH24:MI:SS","HH:MI:SS","HH24:MI","HH:MI"]  # Predefined formats
    output_format = st.selectbox("Select the output format:", output_formats, key="output_format") \
        if conversion_type == "TO_CHAR" else None

    st.subheader("Generated date format")
    
    # Generate the SQL function based on user inputs
    if st.button("Generate"):
        if conversion_type == "TO_DATE":
            if input_string and input_format:
                sql_function = f"TO_DATE({input_string}, '{input_format}')"
                st.code(sql_function, language="sql")
            else:
                st.error("Both input string and format are required for TO_DATE.")
        elif conversion_type == "TO_CHAR":
            if input_string and input_format and output_format:
                sql_function = f"TO_CHAR(TO_DATE({input_string}, '{input_format}'), '{output_format}')"
                st.code(sql_function, language="sql")
            else:
                st.error("Input string, input format, and output format are required for TO_CHAR.")

    # Navigation button to go back to main input page
    if st.button("Back to Main Page"):
        st.session_state.page = "input"  # Set the session state to return to the main input page
        st.rerun()  # Reload the app


