# import streamlit as st

# def render_result_page():
#     st.subheader("IICS Code:")

#     # Get the conditions, logical operators, and result value from session state
#     conditions = st.session_state.get("conditions", [])
#     logical_operators = st.session_state.get("logical_operators", [])
#     result_value = st.session_state.get("result_value", "")

#     # Generate the SQL decode function
#     decode_code = "decode(1,\n"
#     condition_strings = []

#     for idx, condition in enumerate(conditions):
#         db = condition["db"].strip()
#         check = condition["check"].strip().lower()
#         value = condition["value"].strip() if condition["value"] else None

#         if not db or not check:
#             return f"DB and Checks are required for Condition {idx + 1}."

#         if check == "isnull":
#             condition_strings.append(f"ISNULL({db})")
#         elif check == "is not null":
#             condition_strings.append(f"NOT ISNULL({db})")
#         elif check == "equals" and value:
#             condition_strings.append(f"{db} = '{value}'")
#         elif check == "contains" and value:
#             condition_strings.append(f"INSTR({db}, '{value}') > 0")
#         elif check == "starts with" and value:
#             condition_strings.append(f"SUBSTR({db}, 1, {len(value)}) = '{value}'")
#         elif check == "is in list" and value:
#             values = ", ".join([f"'{v.strip()}'" for v in value.split(",")])  # Handle comma-separated list values
#             condition_strings.append(f"IN({db}, {values}, 0)")
#         else:
#             condition_strings.append(f"Invalid condition")

#     # Combine conditions with logical operators
#     combined_conditions = ""
#     for idx, condition_string in enumerate(condition_strings):
#         combined_conditions += condition_string
#         if idx < len(logical_operators):  # Add operator if not the last condition
#             combined_conditions += f" {logical_operators[idx]} "

#     decode_code += f"    {combined_conditions}, '{result_value}'\n)"

#     # Display the generated decode function
#     st.code(decode_code, language="sql")

#     # Allow user to go back to the input page
#     if st.button("Back"):
#         st.session_state.clear()  # Clear session state to reset form
#         st.session_state.page = "input"  # Go back to input page
#         st.rerun()  # Reload the app to reset the page


###################################2nd changes###############################
# import streamlit as st

# # Function to render the result page
# def render_result_page():
#     st.subheader("Generated Decode Code:")

#     conditions = st.session_state.get("conditions", [])

#     # Initialize the DECODE function output
#     decode_code = "decode(1,\n"
    
#     # Loop through all the conditions to build the DECODE code
#     for condition in conditions:
#         condition_strings = []

#         # Process main condition based on check type
#         db = condition['db']
#         check = condition['check']
#         value = condition['value']

#         # Handle condition logic based on the check type
#         if check == "isnull":
#             condition_strings.append(f"ISNULL({db})")
#         elif check == "is not null":
#             condition_strings.append(f"NOT ISNULL({db})")
#         elif check == "equals" and value:
#             condition_strings.append(f"{db} = '{value}'")
#         elif check == "contains" and value:
#             condition_strings.append(f"INSTR({db}, '{value}') > 0")
#         elif check == "starts with" and value:
#             condition_strings.append(f"SUBSTR({db}, 1, {len(value)}) = '{value}'")
#         elif check == "is in list" and value:
#             values = ", ".join([f"'{v.strip()}'" for v in value.split(",")])  # Handle comma-separated list values
#             condition_strings.append(f"IN({db}, {values}, 0)")
#         else:
#             condition_strings.append(f"Invalid condition")

#         # Combine subconditions if any
#         for subcondition in condition['subconditions']:
#             sub_db = subcondition['db']
#             sub_check = subcondition['check']
#             sub_value = subcondition['value']
#             sub_operator = subcondition['operator']

#             if sub_check == "isnull":
#                 condition_strings.append(f" {sub_operator} ISNULL({sub_db})")
#             elif sub_check == "is not null":
#                 condition_strings.append(f" {sub_operator} NOT ISNULL({sub_db})")
#             elif sub_check == "equals" and sub_value:
#                 condition_strings.append(f" {sub_operator} {sub_db} = '{sub_value}'")
#             elif sub_check == "contains" and sub_value:
#                 condition_strings.append(f" {sub_operator} INSTR({sub_db}, '{sub_value}') > 0")
#             elif sub_check == "starts with" and sub_value:
#                 condition_strings.append(f" {sub_operator} SUBSTR({sub_db}, 1, {len(sub_value)}) = '{sub_value}'")
#             elif sub_check == "is in list" and sub_value:
#                 sub_values = ", ".join([f"'{v.strip()}'" for v in sub_value.split(",")])
#                 condition_strings.append(f" {sub_operator} IN({sub_db}, {sub_values}, 0)")
#             else:
#                 condition_strings.append(f" {sub_operator} Invalid subcondition")

#         # Add the condition string with the result value
#         condition_string = " ".join(condition_strings)
#         result = condition['result']
#         decode_code += f"    {condition_string}, '{result}',\n"

#     decode_code += ")"

#     # Display the generated decode function
#     st.code(decode_code, language="sql")

#     # Option to go back to input page
#     if st.button("Back"):
#         st.session_state.clear()  # Clear session state to reset form
#         st.session_state.page = "input"  # Go back to input page
#         st.rerun()  # Reload the app to reset the page

#####################################################
import streamlit as st

# Function to render the result page
def render_result_page():
    st.subheader("Generated Decode Code:")

    conditions = st.session_state.get("conditions", [])

    # Initialize the DECODE function output
    decode_code = "decode(1,\n"
    
    # Loop through all the conditions to build the DECODE code
    for index, condition in enumerate(conditions):
        condition_strings = []

        # Process main condition based on check type
        db = condition['db']
        check = condition['check']
        value = condition['value']

        # Handle condition logic based on the check type
        if check == "isnull":
            condition_strings.append(f"ISNULL({db})")
        elif check == "is not null":
            condition_strings.append(f"NOT ISNULL({db})")
        elif check == "equals" and value:
            condition_strings.append(f"{db} = '{value}'")
        elif check == "contains" and value:
            condition_strings.append(f"INSTR({db}, '{value}') > 0")
        elif check == "starts with" and value:
            condition_strings.append(f"SUBSTR({db}, 1, {len(value)}) = '{value}'")
        elif check == "is in list" and value:
            values = ", ".join([f"'{v.strip()}'" for v in value.split(",")])  # Handle comma-separated list values
            condition_strings.append(f"IN({db}, {values}, 0)")
        else:
            condition_strings.append(f"Invalid condition")

        # Combine subconditions if any
        for subcondition in condition['subconditions']:
            sub_db = subcondition['db']
            sub_check = subcondition['check']
            sub_value = subcondition['value']
            sub_operator = subcondition['operator']

            if sub_check == "isnull":
                condition_strings.append(f" {sub_operator} ISNULL({sub_db})")
            elif sub_check == "is not null":
                condition_strings.append(f" {sub_operator} NOT ISNULL({sub_db})")
            elif sub_check == "equals" and sub_value:
                condition_strings.append(f" {sub_operator} {sub_db} = '{sub_value}'")
            elif sub_check == "contains" and sub_value:
                condition_strings.append(f" {sub_operator} INSTR({sub_db}, '{sub_value}') > 0")
            elif sub_check == "starts with" and sub_value:
                condition_strings.append(f" {sub_operator} SUBSTR({sub_db}, 1, {len(sub_value)}) = '{sub_value}'")
            elif sub_check == "is in list" and sub_value:
                sub_values = ", ".join([f"'{v.strip()}'" for v in sub_value.split(",")])
                condition_strings.append(f" {sub_operator} IN({sub_db}, {sub_values}, 0)")
            else:
                condition_strings.append(f" {sub_operator} Invalid subcondition")

        # Add the condition string with the result value
        condition_string = " ".join(condition_strings)
        result = condition['result']
        
        # Add the condition string to the decode code, adding a comma if it's not the last condition
        if index < len(conditions) - 1:
            decode_code += f"    {condition_string}, '{result}',\n"
        else:
            decode_code += f"    {condition_string}, '{result}'\n"

    decode_code += ")"

    # Display the generated decode function
    st.code(decode_code, language="sql")

    # Option to go back to input page
    if st.button("Back"):
        st.session_state.clear()  # Clear session state to reset form
        st.session_state.page = "input"  # Go back to input page
        st.rerun()  # Reload the app to reset the page
