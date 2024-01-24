import streamlit as st
import pandas as pd

st.title('Real Estate form for creation of dataroom')

development_name = st.text_input('Development name', key='development_name')

st.write('---------')
st.file_uploader('Upload list of purchasers/recipients', type=['csv','xlsx','xlsm'], key='recipient_list')
st.write('Excel file should follow the following format:')
st.markdown('_Purchaser Name | Email | Contact Number | Postal Address | Unit Number (of development)_')

st.write('---------')
st.file_uploader('Upload documents to be shared', accept_multiple_files=True, key=f'shared_documents')

st.write('---------')
if st.button('Submit request'):
    st.write('Submitted')

st.write('---------')
def clear_form():
    for key in st.session_state.keys():
        del st.session_state[key]

if st.button('Clear form'):
    clear_form()

if __name__ == '__main__':     st.set_option('server.enableCORS', True) 
