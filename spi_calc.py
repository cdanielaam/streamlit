import streamlit as st
import pandas as pd
import numpy as np

st.title('Spirometry Calculator')

#patient_ID = st.number_input('Enter Patient ID:', 0,999999999)


with st.form(key='spirometry_data'):
    gender = st.selectbox('Select gender:', ['Boy', 'Girl'])
    height = st.number_input('Enter height:', 0,200)
    weight = st.number_input('Enter weight:', 0,100)
    age = st.number_input('Enter age:', 0,15)
    FVC = st.number_input(label='Enter measured FVC:', step=1., format="%.2f")
    FEV1 = st.number_input('Enter measured FEV1:', step=1., format="%.2f")
    FEF2575 = st.number_input('Enter measured FEF2575:', step=1., format="%.2f")
    st.form_submit_button('Calculate')


if gender == 'Boy':
    st.write('Yesssss!')
elif gender == 'Girl':
    st.write('NOOOOOO')
