# import streamlit as st
# import pandas as pd
# from db_elements import db_elements
# from result_page import render_result_page
# from date_conversion import render_date_conversion_page
# from io import BytesIO

# # Set the layout to wide mode and set a custom favicon
# st.set_page_config(
#     layout="wide",
#     page_icon="favicon.ico"  # Set your favicon file here, make sure it's in the same directory or provide a relative/absolute path
# )

# st.image("image.png", width=200)

# # Initialize session state variables if they don't exist yet
# if "conditions" not in st.session_state:
#     st.session_state.conditions = []
# if "logical_operators" not in st.session_state:
#     st.session_state.logical_operators = []
# if "condition_count" not in st.session_state:
#     st.session_state.condition_count = 1  # Default to 1 condition
# if "page" not in st.session_state:
#     st.session_state.page = "input"  # Default to input page


# # Function to export conditions to Excel
# def export_to_excel():
#     """Export conditions to an Excel file."""
#     conditions_data = []
#     for condition in st.session_state.conditions:
#         for subcondition in condition["subconditions"]:
#             conditions_data.append({
#                 "Main DB Element": condition["db"],
#                 "Main Condition Check": condition["check"],
#                 "Main Condition Value": condition["value"],
#                 "Subcondition DB Element": subcondition["db"],
#                 "Subcondition Check": subcondition["check"],
#                 "Subcondition Value": subcondition["value"],
#                 "Subcondition Operator": subcondition["operator"],
#                 "Result": condition["result"]
#             })
    
#     df = pd.DataFrame(conditions_data)
#     # Save the DataFrame to a BytesIO object
#     excel_file = BytesIO()
#     with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
#         df.to_excel(writer, index=False, sheet_name="Conditions")
#     excel_file.seek(0)
#     return excel_file


# # Function to parse conditions from uploaded Excel
# def parse_conditions_from_excel(uploaded_file):
#     """Parse conditions from the uploaded Excel file."""
#     try:
#         data = pd.read_excel(uploaded_file)
#         conditions = []
        
#         for _, row in data.iterrows():
#             # Assuming the columns in your Excel are as follows:
#             # Main DB Element, Main Condition Check, Main Condition Value, Subcondition DB Element, etc.
#             condition = {
#                 "db": row["Main DB Element"],
#                 "check": row["Main Condition Check"],
#                 "value": row["Main Condition Value"],
#                 "result": row["Result"],
#                 "subconditions": [{
#                     "db": row["Subcondition DB Element"],
#                     "check": row["Subcondition Check"],
#                     "value": row["Subcondition Value"],
#                     "operator": row["Subcondition Operator"]
#                 }] if pd.notnull(row["Subcondition DB Element"]) else []
#             }
#             conditions.append(condition)
        
#         return conditions
#     except Exception as e:
#         st.error(f"Error parsing conditions from Excel: {e}")
#         return []


# def render_input_page():
#     """Render the input page."""
#     st.title("Decode Generator")

#     # Add a file uploader for Excel input
#     st.subheader("Upload Excel File (Optional)")
#     uploaded_file = st.file_uploader("Upload an Excel file with conditions", type=["xlsx", "xls"])

#     if uploaded_file:
#         st.session_state.conditions = parse_conditions_from_excel(uploaded_file)
#         st.write("Preview of uploaded data:")
#         st.write(st.session_state.conditions)
#         st.success("Conditions loaded successfully from the uploaded file!")

#     # Get the condition count from the widget
#     condition_count = st.number_input(
#         "Enter the number of conditions:", 
#         min_value=1, 
#         step=1, 
#         value=st.session_state.condition_count, 
#         key="condition_count"
#     )

#     # Update the condition list size to match the condition count
#     while len(st.session_state.conditions) < condition_count:
#         st.session_state.conditions.append({
#             "db": db_elements[0],
#             "check": "equals",
#             "value": "",
#             "subconditions": [],
#             "result": ""
#         })
#     while len(st.session_state.conditions) > condition_count:
#         st.session_state.conditions.pop()

#     for i in range(condition_count):
#         st.subheader(f"Condition - {i + 1}")
        
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.session_state.conditions[i]["db"] = st.selectbox(
#                 f"Main Condition DB Element {i + 1}:",
#                 db_elements,
#                 key=f"db_{i}",
#                 index=db_elements.index(st.session_state.conditions[i]["db"])
#             )
#         with col2:
#             st.session_state.conditions[i]["check"] = st.selectbox(
#                 f"Main Condition Check {i + 1}:",
#                 ["equals", "isnull", "is not null", "starts with", "contains", "is in list"],
#                 key=f"check_{i}",
#                 index=["equals", "isnull", "is not null", "starts with", "contains", "is in list"].index(
#                     st.session_state.conditions[i]["check"]
#                 )
#             )
#         with col3:
#             if st.session_state.conditions[i]["check"] not in ["isnull", "is not null"]:
#                 st.session_state.conditions[i]["value"] = st.text_input(
#                     f"Main Condition Value {i + 1}:",
#                     key=f"value_{i}",
#                     value=st.session_state.conditions[i]["value"]
#                 )

#         # Subconditions (allow multiple subconditions)
#         subconditions = st.session_state.conditions[i]["subconditions"]
#         add_subcondition = st.checkbox(f"Add subconditions for Condition {i + 1}", key=f"subcondition_checkbox_{i}")
        
#         if add_subcondition:
#             subcondition_count = st.number_input(
#                 f"Enter the number of subconditions for Condition {i + 1}:",
#                 min_value=1,
#                 step=1,
#                 value=len(subconditions) or 1,
#                 key=f"subcondition_count_{i}"
#             )
#             while len(subconditions) < subcondition_count:
#                 subconditions.append({"db": db_elements[0], "check": "equals", "value": "", "operator": "AND"})
#             while len(subconditions) > subcondition_count:
#                 subconditions.pop()

#             for j, sub in enumerate(subconditions):
#                 col1, col2, col3, col4 = st.columns(4)
#                 with col1:
#                     sub["db"] = st.selectbox(
#                         f"Subcondition {j + 1} DB Element:",
#                         db_elements,
#                         key=f"sub_db_{i}_{j}",
#                         index=db_elements.index(sub["db"])
#                     )
#                 with col2:
#                     sub["check"] = st.selectbox(
#                         f"Subcondition {j + 1} Check:",
#                         ["equals", "isnull", "is not null", "starts with", "contains", "is in list"],
#                         key=f"sub_check_{i}_{j}",
#                         index=["equals", "isnull", "is not null", "starts with", "contains", "is in list"].index(sub["check"])
#                     )
#                 with col3:
#                     if sub["check"] not in ["isnull", "is not null"]:
#                         sub["value"] = st.text_input(
#                             f"Subcondition {j + 1} Value:",
#                             key=f"sub_value_{i}_{j}",
#                             value=sub["value"]
#                         )
#                 with col4:
#                     sub["operator"] = st.selectbox(
#                         f"Subcondition {j + 1} Logical Operator:",
#                         ["AND", "OR"],
#                         key=f"sub_operator_{i}_{j}",
#                         index=["AND", "OR"].index(sub["operator"])
#                     )

#         # Result for this condition
#         st.session_state.conditions[i]["result"] = st.text_input(
#             f"Enter Result Value for Condition {i + 1}:",
#             key=f"result_value_{i}",
#             value=st.session_state.conditions[i]["result"]
#         )

#     # Button to export the conditions to Excel
#     if st.button("Download Excel File"):
#         excel_file = export_to_excel()
#         st.download_button(
#             label="Download Excel",
#             data=excel_file,
#             file_name="conditions.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )

#     # Navigation buttons
#     if st.button("Generate Decode"):
#         st.session_state.page = "result"
#         st.rerun()

#     if st.button("Go to Date Conversion"):
#         st.session_state.page = "date_conversion"
#         st.rerun()


# # Main app function to control navigation
# def main():
#     if st.session_state.page == "input":
#         render_input_page()
#     elif st.session_state.page == "date_conversion":
#         render_date_conversion_page()
#     elif st.session_state.page == "result":
#         if st.button("Back to Input"):
#             st.session_state.page = "input"
#             st.rerun()
#         render_result_page()


# if __name__ == "__main__":
#     main()
