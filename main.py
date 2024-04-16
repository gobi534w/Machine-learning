import streamlit as st
import numpy as np
import pandas as pd

# Loading Data from a CSV File
@st.cache
def load_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except FileNotFoundError:
        st.error("File not found. Please make sure the file exists.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Data loaded successfully!")  # Debugging statement
else:
    st.warning("Please upload a CSV file.")

if 'data' in locals() and data is not None:  # Check if 'data' is defined and not None
    # Separating concept features from Target
    concepts = np.array(data.iloc[:, :-1])

    # Isolating target into a separate DataFrame
    target = np.array(data.iloc[:, -1])

    def learn(concepts, target):
        '''
        learn() function implements the learning method of the Candidate elimination algorithm.
        Arguments:
            concepts - a data frame with all the features
            target - a data frame with corresponding output values
        '''
        # Remaining code for learn() function as before...

    # Call the function to learn
    s_final, g_final = learn(concepts, target)

    # Streamlit UI
    st.write("Final Specific_h:")
    st.write(s_final)

    st.write("Final General_h:")
    st.write(g_final)
