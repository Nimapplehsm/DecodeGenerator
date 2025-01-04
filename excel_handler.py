import streamlit as st
import pandas as pd

# Set up file upload and fix data types
@st.cache_data
def load_excel(file):
    """Load and clean data from an Excel file."""
    try:
        data = pd.read_excel(file)

        # Check and clean data types
        st.write("Data Types Before Fixing:", data.dtypes)

        # Handle NaN values
        data = data.fillna('')

        # Convert all columns to string type
        for column in data.columns:
            data[column] = data[column].astype(str)

        # Check again after conversion
        st.write("Data Types After Fixing:", data.dtypes)
        return data
    except Exception as e:
        st.error(f"Error loading Excel file: {e}")
        return pd.DataFrame()

def render_input_page():
    """Render the input page."""
    st.title("Decode Generator")

    # Add a file uploader for Excel input
    st.subheader("Upload Excel File (Optional)")
    uploaded_file = st.file_uploader("Upload an Excel file with conditions", type=["xlsx", "xls"])
    
    if uploaded_file:
        data = load_excel(uploaded_file)
        st.write("Preview of uploaded data:")
        st.write(data)

    # Other form handling code...
