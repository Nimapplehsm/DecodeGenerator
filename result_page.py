import re
import streamlit as st

def parse_group_condition(condition_string):
    """Parse the main condition (before the first subcondition)."""
    match = re.match(r"(\S+)\s(\S+)\s\"(.+)\"", condition_string.strip())
    if match:
        db = match.group(1)
        check = match.group(2)
        value = match.group(3)
        return db, check, value
    return None, None, None

def parse_condition(condition_string):
    """Helper to parse individual conditions into db, check, and value."""
    match = re.match(r"(\S+)\s(\S+)\s\"(.+)\"", condition_string.strip())
    if match:
        db = match.group(1)
        check = match.group(2)
        value = match.group(3)
        return db, check, value
    return None, None, None

def parse_subconditions(subcondition_string):
    """Parse the subconditions that might contain multiple parts like 'OR' or 'AND'."""
    subconditions = []
    
    # Split the subcondition part by operator (AND/OR) while keeping operators as part of the subcondition
    parts = re.split(r"(OR|AND)", subcondition_string)
    for i in range(0, len(parts), 2):
        condition = parts[i].strip()
        operator = parts[i+1].strip() if i+1 < len(parts) else "AND"  # Default operator is AND
        db, check, value = parse_condition(condition)
        
        subconditions.append({
            "db": db,
            "check": check,
            "value": value,
            "operator": operator
        })
    
    return subconditions

def parse_full_condition(group_condition, subcondition_string):
    """Parse the full condition including both group and subconditions."""
    db, check, value = parse_group_condition(group_condition)
    subconditions = parse_subconditions(subcondition_string)
    
    return {
        "group_condition": group_condition,
        "subconditions": subconditions,
        "result": value  # Assuming the result value is same as the main condition's value for now
    }

def parse_condition_value(check, value):
    """
    Parse the subcondition value for each condition.
    Returns the parsed check and value.
    """
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    
    return check, value

# Function to render the result page
def render_result_page():
    st.subheader("Generated Decode Code:")

    conditions = st.session_state.get("conditions", [])
    Fileconditions = st.session_state.get("Fileconditions", [])
    # st.write(st.session_state)

    if conditions != []:
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
        
    elif Fileconditions != []:
        # Initialize the DECODE function output
        decode_code = "decode(1,\n"
        
        # Loop through all the conditions to build the DECODE code
        for index, condition in enumerate(Fileconditions):
            condition_strings = []

            # Process main condition based on check type
            group_condition = condition['group_condition']
            subconditions = condition['subconditions']
            result = condition['result']

            # Parse the main condition (group_condition)
            db, check, value = parse_condition(group_condition)

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
                values = ", ".join([f"'{v.strip()}'" for v in value.split(",")])
                condition_strings.append(f"IN({db}, {values}, 0)")

            # Process subconditions
            for subcondition in subconditions:
                # st.write(subcondition)
                sub_db = subcondition['db']
                sub_check = subcondition['check']
                sub_value = subcondition['value']
                sub_operator = subcondition['operator']

                # Parse the subcondition value
                sub_check, sub_value = parse_condition_value(sub_check, sub_value)

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
            # st.write(condition_strings)
            # Combine condition strings and add the result
            condition_string = " ".join(condition_strings)
            decode_code += f"    {condition_string}, '{result}'\n" if index < len(Fileconditions) - 1 else f"    {condition_string}, '{result}'\n"

            decode_code += ")"

        # Display the generated decode function
        st.code(decode_code, language="sql")
    
    # Option to go back to input page
    if st.button("Back"):
        st.session_state.clear()  # Clear session state to reset form
        st.session_state.page = "input"  # Go back to input page
        st.rerun()  # Reload the app to reset the page
