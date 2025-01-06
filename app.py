import streamlit as st
import pandas as pd
from io import BytesIO
from db_elements import db_elements
from result_page import render_result_page
from date_conversion import render_date_conversion_page

# Set the layout to wide mode and set a custom favicon
st.set_page_config(
    layout="wide",
    page_icon="favicon.ico"
)

st.image("image.png", width=200)

# Initialize session state variables if they don't exist yet
if "conditions" not in st.session_state:
    st.session_state.conditions = []
if "logical_operators" not in st.session_state:
    st.session_state.logical_operators = []
if "condition_count" not in st.session_state:
    st.session_state.condition_count = 1
if "page" not in st.session_state:
    st.session_state.page = "input"


@st.cache_data
def load_excel(file):
    """Load data from an Excel file."""
    return pd.read_excel(file)


def create_sample_template():
    """Create a sample Excel template for download."""
    sample_data = {
        "Group Condition": [
            'DB Element Check "Value"',
            'DB Element Check "Value"',
            'DB Element Check "Value"'
        ],
        "Subcondition": [
            '(Subcondition DB Element Subcondition Check "Subcondition Value") AND',
            '(Subcondition DB Element Subcondition Check "Subcondition Value") OR',
            '(Subcondition DB Element Subcondition Check "Subcondition Value") AND'
        ],
        "Result": [
            'result1',
            'result2',
            'result3'
        ]
    }
    df = pd.DataFrame(sample_data)
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Template")
    buffer.seek(0)
    return buffer


def decode_conditions(conditions):
    """Decode the conditions into a structured string."""
    decoded_conditions = []
    for condition in conditions:
        # Build main condition part: DB Element Check Value
        main_condition = f'{condition["group_condition"]}'
        
        # Build subcondition part
        subconditions = []
        for sub in condition.get("subconditions", []):
            sub_condition = f'{sub["db"]} {sub["check"]} "{sub["value"]}"' if sub["value"] else f'{sub["db"]} {sub["check"]}'
            subconditions.append(f'{sub_condition} {sub["operator"]}')
        
        # Combine main condition and subconditions
        subcondition_str = " ".join(subconditions).strip()
        full_condition = f'{main_condition} {"AND " + subcondition_str if subcondition_str else ""}'

        # Add result to the full condition
        decoded_conditions.append(f'IF {full_condition} THEN {condition["result"]}')
    
    return decoded_conditions

def parse_condition(condition_string):
    """Parse the condition string (like `ProtocolCode equals "ASK-CHF2-CS201"`) into its components."""
    db, check_value = condition_string.split(" ", 1)
    check, value = check_value.split(" ", 1)
    
    # Remove extra quotes from values
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    
    return db, check, value

# Function to split the subcondition string into individual subconditions
def split_subconditions(subcondition_string):
    """Split a subcondition string into a list of individual subconditions."""
    # We can split on " OR " or " AND ", and clean the string for subcondition parsing
    subcondition_parts = []
    for operator in [" OR ", " AND "]:
        parts = subcondition_string.split(operator)
        if len(parts) > 1:
            subcondition_parts = parts
            break
    
    # Clean each part by removing parentheses and trimming spaces
    cleaned_parts = [part.strip().strip("()") for part in subcondition_parts]
    return cleaned_parts

# Function to parse subconditions (like `ContainerSpecimenClass starts with "SM01"`)
def parse_subcondition(subcondition):
    """Parse a subcondition string into its db, check, value, and operator."""
    # Example format: `ContainerSpecimenClass starts with "SM01"`
    sub_db, sub_check_value = subcondition.split(" ", 1)
    
    sub_check_parts = sub_check_value.split(" ", 1)

    # sub_check will be the first part (the full check type)
    sub_check = sub_check_parts[0] + " " + sub_check_parts[1].split(" ", 1)[0]

    # sub_value will be the value part, i.e., the part after "starts with" (strip surrounding quotes)
    sub_value = sub_check_value.split(" ", 1)[1]
    sub_value = sub_value.split(" ", 1)[1]

    # st.write(sub_check_value)
    # st.write(sub_check)
    # st.write(sub_value)
    # Remove quotes from value
    if sub_value.startswith('"') and sub_value.endswith('"'):
        sub_value = sub_value[1:-1]
    # st.write(sub_value)
    # Determine the operator (either OR or AND)
    operator = "AND" if "AND" in subcondition else "OR"
    # st.write(sub_db)
    
    # st.write(operator)
    return sub_db, sub_check, sub_value, operator

def render_input_page():
    """Render the input page."""
    st.title("Decode Generator")

    input_mode = st.selectbox("Select Input Mode:", ["Upload Excel File", "Enter Values Directly"], key="input_mode")

    if input_mode == "Upload Excel File":
        st.subheader("Upload Excel File")

        # Provide a download button for the sample template
        st.download_button(
            label="Download Sample Template",
            data=create_sample_template(),
            file_name="sample_template.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        uploaded_file = st.file_uploader("Upload an Excel file with conditions", type=["xlsx", "xls"])

        if uploaded_file:
            data = load_excel(uploaded_file)
            st.write("Preview of uploaded data:")
            st.write(data)

            # Convert uploaded data into conditions
            st.session_state.Fileconditions = []
            for _, row in data.iterrows():
                # Extract the Group Condition (Main Condition)
                group_condition = row["Group Condition"]
                
                # Parse the main condition to get db, check, and value
                main_db, main_check, main_value = parse_condition(group_condition)

                # Extract the subcondition (Subcondition column)
                subcondition_string = row["Subcondition"]
                subconditions = []

                # Split subconditions by "OR" or "AND"
                subcondition_parts = split_subconditions(subcondition_string)

                # Parse each subcondition and add to the list
                for i, subcondition in enumerate(subcondition_parts):
                    sub_db, sub_check, sub_value, operator = parse_subcondition(subcondition)
                    subconditions.append({
                        "db": sub_db,
                        "check": sub_check,
                        "value": sub_value,
                        "operator": operator
                    })

                # Store the condition (group + subconditions)
                condition = {
                    "group_condition": group_condition,
                    "subconditions": subconditions,
                    "result": row["Result"]
                }

                st.session_state.Fileconditions.append(condition)
                # st.write(st.session_state)

    elif input_mode == "Enter Values Directly":
        st.subheader("Enter Values Directly")
        
        # Get the condition count from the widget
        condition_count = st.number_input(
            "Enter the number of conditions:", 
            min_value=1, 
            step=1, 
            value=st.session_state.condition_count, 
            key="condition_count"
        )

        # Update the condition list size to match the condition count
        while len(st.session_state.conditions) < condition_count:
            st.session_state.conditions.append({
                "db": db_elements[0],
                "check": "equals",
                "value": "",
                "subconditions": [],
                "result": ""
            })
        while len(st.session_state.conditions) > condition_count:
            st.session_state.conditions.pop()

        for i in range(condition_count):
            st.subheader(f"Condition - {i + 1}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.session_state.conditions[i]["db"] = st.selectbox(
                    f"Main Condition DB Element {i + 1}:",
                    db_elements,
                    key=f"db_{i}",
                    index=db_elements.index(st.session_state.conditions[i]["db"])
                )
            with col2:
                st.session_state.conditions[i]["check"] = st.selectbox(
                    f"Main Condition Check {i + 1}:",
                    ["equals", "isnull", "is not null", "starts with", "contains", "is in list"],
                    key=f"check_{i}",
                    index=["equals", "isnull", "is not null", "starts with", "contains", "is in list"].index(
                        st.session_state.conditions[i]["check"]
                    )
                )
            with col3:
                if st.session_state.conditions[i]["check"] not in ["isnull", "is not null"]:
                    st.session_state.conditions[i]["value"] = st.text_input(
                        f"Main Condition Value {i + 1}:",
                        key=f"value_{i}",
                        value=st.session_state.conditions[i]["value"]
                    )

            # Subconditions (allow multiple subconditions)
            subconditions = st.session_state.conditions[i]["subconditions"]
            add_subcondition = st.checkbox(f"Add subconditions for Condition {i + 1}", key=f"subcondition_checkbox_{i}")
            
            if add_subcondition:
                subcondition_count = st.number_input(
                    f"Enter the number of subconditions for Condition {i + 1}:",
                    min_value=1,
                    step=1,
                    value=len(subconditions) or 1,
                    key=f"subcondition_count_{i}"
                )
                while len(subconditions) < subcondition_count:
                    subconditions.append({"db": db_elements[0], "check": "equals", "value": "", "operator": "AND"})
                while len(subconditions) > subcondition_count:
                    subconditions.pop()

                for j, sub in enumerate(subconditions):
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        sub["db"] = st.selectbox(
                            f"Subcondition {j + 1} DB Element:",
                            db_elements,
                            key=f"sub_db_{i}_{j}",
                            index=db_elements.index(sub["db"])
                        )
                    with col2:
                        sub["check"] = st.selectbox(
                            f"Subcondition {j + 1} Check:",
                            ["equals", "isnull", "is not null", "starts with", "contains", "is in list"],
                            key=f"sub_check_{i}_{j}",
                            index=["equals", "isnull", "is not null", "starts with", "contains", "is in list"].index(sub["check"])
                        )
                    with col3:
                        if sub["check"] not in ["isnull", "is not null"]:
                            sub["value"] = st.text_input(
                                f"Subcondition {j + 1} Value:",
                                key=f"sub_value_{i}_{j}",
                                value=sub["value"]
                            )
                    with col4:
                        sub["operator"] = st.selectbox(
                            f"Subcondition {j + 1} Logical Operator:",
                            ["AND", "OR"],
                            key=f"sub_operator_{i}_{j}",
                            index=["AND", "OR"].index(sub["operator"])
                        )

            # Result for this condition
            st.session_state.conditions[i]["result"] = st.text_input(
                f"Enter Result Value for Condition {i + 1}:",
                key=f"result_value_{i}",
                value=st.session_state.conditions[i]["result"]
            )

    # Navigation buttons
    if st.button("Generate Decode"):
        st.session_state.page = "result"
        st.rerun()

    if st.button("Go to Date Conversion"):
        st.session_state.page = "date_conversion"
        st.rerun()


def main():
    if st.session_state.page == "input":
        render_input_page()
    elif st.session_state.page == "date_conversion":
        render_date_conversion_page()
    elif st.session_state.page == "result":
        if st.button("Back to Input"):
            st.session_state.page = "input"
            st.rerun()
        render_result_page()


if __name__ == "__main__":
    main()
