import streamlit as st
import pickle

st.title('Movie Recommendation System')

option = st.selectbox(
    'How would you like to contacted?',
    ('Email', 'Home Phone', 'Mobile Phone')
)