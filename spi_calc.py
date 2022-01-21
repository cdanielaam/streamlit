import streamlit as st
import pandas as pd
import numpy as np

st.title('Spirometry Calculator')
st.write('Based on: "Development and Validation of Predictive Equations for Spirometry in Portuguese Children, 2022"')
st.write("This APP should only be used for children aged between xx and xx, and height between xxx and xxx")

#patient_ID = st.number_input('Enter Patient ID:', 0,999999999)

coll1, coll2 = st.columns(2)

with st.form(key='spirometry_data'):
    gender = st.selectbox('Select gender:', ['Boy', 'Girl'])
    with coll1: 
        height = st.number_input('Enter height:', 0,200)
        weight = st.number_input('Enter weight:', 0,100)
        age = st.number_input('Enter age:', 0,15)
    with coll2:
        FVC = st.number_input(label='Enter measured FVC:', step=1., format="%.2f")
        FEV1 = st.number_input('Enter measured FEV1:', step=1., format="%.2f")
        FEF2575 = st.number_input('Enter measured FEF2575:', step=1., format="%.2f")
    st.form_submit_button('Calculate')
    
col1, col2, col3, col4 = st.columns(4)

#col1.subheader("Predicted:")
#col2.subheader("Predicted %:")
#col3.subheader("LLN values:")
#col4.subheader("Z-Score:")

if gender == 'Boy':
    #FVC:
    predicted_fvc_boys = -2.322603 + (0.030837*float(height)) + (0.00305*float(weight)) + (0.009612*float(age))
    with col1: 
        st.write("Predicted FVC: ")
        st.write(round(predicted_fvc_boys, 2))
    result_percent_fvc_boys = (float(FVC)/float(predicted_fvc_boys))*100
    with col2: 
        st.write("% FVC: ")
        st.write(round(result_percent_fvc_boys, 2))
    result_lln_fvc_boys = float(predicted_fvc_boys)-(1.64*0.34)
    with col3: 
        st.write("LLN FVC: ")
        st.write(round(result_lln_fvc_boys, 2))
    result_zscore_fvc_boys = (float(FVC)-float(predicted_fvc_boys))/0.34
    with col4: 
        st.write("Z-Score FVC: ") 
        st.write(round(result_zscore_fvc_boys, 2))
    #FEV1:
    result_fev1_boys = -2.03101 + (0.02710*float(height)) + (0.02203*float(age))
    with col1: 
        st.write("Predicted FEV1: ")
        st.write(round(result_fev1_boys, 2))
    result_percent_fev1_boys = (float(FEV1)/float(result_fev1_boys))*100
    with col2: 
        st.write("% FEV1: ")
        st.write(round(result_percent_fev1_boys, 2))
    result_lln_fev1_boys = float(result_fev1_boys)-(1.64*0.29)
    with col3: 
        st.write("LLN FEV1: ")
        st.write(round(result_lln_fev1_boys, 2))
    result_zscore_fev1_boys = (float(FEV1)-float(result_fev1_boys))/0.29
    with col4: 
        st.write("Z-Score FEV1: ")
        st.write(round(result_zscore_fev1_boys, 2))
    #FEF2575:
    result_fef2575_boys = 0.4493680  - (0.0001922*float(height)) + (0.0510957*float(age)) + (0.6790825*float(FVC))
    with col1: 
        st.write("Predicted FEF25/75: ")
        st.write(round(result_fef2575_boys, 2))
    result_percent_fef2575_boys = (float(FEF2575)/float(result_fef2575_boys))*100
    with col2: 
        st.write("% FEF25/75: ")
        st.write(round(result_percent_fef2575_boys, 2))
    result_lln_fef2575_boys = float(result_fef2575_boys)-(1.64*0.53)
    with col3: 
        st.write("LLN FEF25/75: ")
        st.write(round(result_lln_fef2575_boys, 2))
    result_zscore_fef2575_boys = (float(FEF2575)-float(result_fef2575_boys))/0.53
    with col4: 
        st.write("Z-Score FEF25/75: ") 
        st.write(round(result_zscore_fef2575_boys, 2))
    #FEV1/FVC:
    result_fev1fvc_boys = "89.96 (85.31-94.61)"
    with col1: 
        st.write("Predicted FEV1/FVC: ")
        st.write(result_fev1fvc_boys)
    result_percent_fev1fvc_boys = (((float(FEV1))/(float(FVC))/89.96)*100)*100
    with col2: 
        st.write("% FEV1/FVC: ")
        st.write(round(result_percent_fev1fvc_boys, 2))
    result_lln_fev1fvc_boys = 82.334
    with col3: 
        st.write("LLN FEV1/FVC: ")
        st.write(round(result_lln_fev1fvc_boys, 2))
    result_zscore_fev1fvc_boys = ((float(FEV1)/float(FVC)*100)-89.96)/4.65
    with col4: 
        st.write("Z-Score FEV1/FVC: ") 
        st.write(round(result_zscore_fev1fvc_boys, 2))
        #Auto Report:
    if ((float(result_zscore_fvc_boys) >= -1.64) and (float(result_zscore_fev1_boys) >= -1.64) and (float(result_zscore_fef2575_boys) >= -1.64) and (float(result_zscore_fev1fvc_boys) >= -1.64)): #normal spirometry for boys
        st.write("All parameters are within normal range.")
    elif ((float(result_zscore_fvc_boys) < -1.64) and (float(result_zscore_fef2575_boys) >= -1.64) and (float(result_zscore_fev1fvc_boys) >= -1.64)): #restrictive pattern boys
        st.write("Forced Vital Capacity is bellow the 5th percentile. This suggests a restrictive pattern and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_boys) >= -1.64) and (float(result_zscore_fef2575_boys) < -1.64) and (float(result_zscore_fev1fvc_boys) >= -1.64)): #small airways obstruction boys
        st.write("FEF25-75 is bellow the 5th percentile. This suggests small airways obstruction and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_boys) >= -1.64) and (float(result_zscore_fev1fvc_boys) < -1.64)): #obstructive pattern boys
        st.write("FEV1/FVC ratio is bellow the 5th percentile. This suggests an obstructive pattern and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_boys) < -1.64) and (float(result_zscore_fev1fvc_boys) <-1.64)): #mixed pattern boys
        st.write("Forced Vital Capacity and FEV1/FVC ratio are bellow the 5th percentile. This suggests a mixed pattern and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_boys) >= -1.64) and (float(result_zscore_fev1_boys) < -1.64) and (float(result_zscore_fef2575_boys) >= -1.64) and (float(result_zscore_fev1fvc_boys) >= -1.64)): #FEV1 not specific pattern boys
        st.write("Forced Expiratory Volume in the first second is bellow the 5th percentile. This is an unspecific finding and deserves further medical investigation.")
elif gender == 'Girl':
    #FVC:
    predicted_fvc_girls = -3.897335 + (0.040381*float(height)) - (0.02474*float(weight)) + (0.06740*(float(weight)/((float(height)/100)*float(height)/100)))
    with col1: 
        st.write("Predicted FVC: ")
        st.write(round(predicted_fvc_girls, 2))
    result_percent_fvc_girls = (float(FVC)/float(predicted_fvc_girls))*100
    with col2: 
        st.write("% FVC: ")
        st.write(round(result_percent_fvc_girls, 2))
    result_lln_fvc_girls = float(predicted_fvc_girls)-(1.64*0.33)
    with col3: 
        st.write("LLN FVC: ")
        st.write(round(result_lln_fvc_girls, 2))
    result_zscore_fvc_girls = (float(FVC)-float(predicted_fvc_girls))/0.33
    with col4: 
        st.write("Z-Score FVC: ") 
        st.write(round(result_zscore_fvc_girls, 2))
    #FEV1:
    result_fev1_girls = -3.012830 + (0.030310*float(height)) - (0.015603*float(weight)) + (0.035593*float(age)) + (0.049651*(float(weight)/((float(height)/100)*float(height)/100)))
    with col1: 
        st.write("Predicted FEV1: ")
        st.write(round(result_fev1_girls, 2))
    result_percent_fev1_girls = (float(FEV1)/float(result_fev1_girls))*100
    with col2: 
        st.write("% FEV1: ")
        st.write(round(result_percent_fev1_girls, 2))
    result_lln_fev1_girls = float(result_fev1_girls)-(1.64*0.30)
    with col3: 
        st.write("LLN FEV1: ")
        st.write(round(result_lln_fev1_girls, 2))
    result_zscore_fev1_girls = (float(FEV1)-float(result_fev1_girls))/0.30
    with col4: 
        st.write("Z-Score FEV1: ")
        st.write(round(result_zscore_fev1_girls, 2))
    #FEF2575:
    result_fef2575_girls = -1.23855 + (0.01240*float(height)) - (0.01284*float(weight)) + (0.74267*float(FVC)) + (0.04417*(float(weight)/((float(height)/100)*float(height)/100)))
    with col1: 
        st.write("Predicted FEF25/75: ")
        st.write(round(result_fef2575_girls, 2))
    result_percent_fef2575_girls = (float(FEF2575)/float(result_fef2575_girls))*100
    with col2: 
        st.write("% FEF25/75: ")
        st.write(round(result_percent_fef2575_girls, 2))
    result_lln_fef2575_girls = float(result_fef2575_girls)-(1.64*0.53)
    with col3: 
        st.write("LLN FEF25/75: ")
        st.write(round(result_lln_fef2575_girls, 2))
    result_zscore_fef2575_girls = (float(FEF2575)-float(result_fef2575_girls))/0.53
    with col4: 
        st.write("Z-Score FEF25/75: ") 
        st.write(round(result_zscore_fef2575_girls, 2))
    #FEV1/FVC:
    result_fev1fvc_girls = "90.81 (86.18-95.44)"
    with col1: 
        st.write("Predicted FEV1/FVC: ")
        st.write(result_fev1fvc_girls)
    result_percent_fev1fvc_girls = (((float(FEV1))/(float(FVC))/90.81)*100)*100
    with col2: 
        st.write("% FEV1/FVC: ")
        st.write(round(result_percent_fev1fvc_girls, 2))
    result_lln_fev1fvc_girls = 83.2168
    with col3: 
        st.write("LLN FEV1/FVC: ")
        st.write(round(result_lln_fev1fvc_girls, 2))
    result_zscore_fev1fvc_girls = ((float(FEV1)/float(FVC)*100)-90.81)/4.63
    with col4: 
        st.write("Z-Score FEV1/FVC: ") 
        st.write(round(result_zscore_fev1fvc_girls, 2))
        #Auto Report:
    if ((float(result_zscore_fvc_girls) >= -1.64) and (float(result_zscore_fev1_girls) >= -1.64) and (float(result_zscore_fef2575_girls) >= -1.64) and (float(result_zscore_fev1fvc_girls) >= -1.64)): #normal spirometry for girls
        st.write("All parameters are within normal range.")
    elif ((float(result_zscore_fvc_girls) < -1.64) and (float(result_zscore_fef2575_girls) >= -1.64) and (float(result_zscore_fev1fvc_girls) >= -1.64)): #restrictive pattern girls
        st.write("Forced Vital Capacity is bellow the 5th percentile. This suggests a restrictive pattern and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_girls) >= -1.64) and (float(result_zscore_fef2575_girls) < -1.64) and (float(result_zscore_fev1fvc_girls) >= -1.64)): #small airways obstruction girls
        st.write("FEF25-75 is bellow the 5th percentile. This suggests small airways obstruction and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_girls) >= -1.64) and (float(result_zscore_fev1fvc_girls) < -1.64)): #obstructive pattern girls
        st.write("FEV1/FVC ratio is bellow the 5th percentile. This suggests an obstructive pattern and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_girls) < -1.64) and (float(result_zscore_fev1fvc_girls) <-1.64)): #mixed pattern girls
        st.write("Forced Vital Capacity and FEV1/FVC ratio are bellow the 5th percentile. This suggests a mixed pattern and deserves further medical investigation.")
    elif ((float(result_zscore_fvc_girls) >= -1.64) and (float(result_zscore_fev1_girls) < -1.64) and (float(result_zscore_fef2575_girls) >= -1.64) and (float(result_zscore_fev1fvc_girls) >= -1.64)): #FEV1 not specific pattern girls
        st.write("Forced Expiratory Volume in the first second is bellow the 5th percentile. This is an unspecific finding and deserves further medical investigation.")

st.button('Print PDF')