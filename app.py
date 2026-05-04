# app.py
# ---------1.Load Libraries-----------------------
import streamlit as st
import numpy as np
import pickle
from sklearn.datasets import load_breast_cancer

## -----------------2.load and save model and scalar-----------------
with open("model.pkl",'rb') as f:
  model=pickle.load(f)
with open("scalar.pkl",'rb') as f:
  model=pickle.load(f)

###  --------------3.app title and description--------------
st.title("Breast Cancer Prediction App")
st.write("This app predicts whether a tumer is malignanat or bengin based on input features.")

## -----------4.Load feature names----------
data=load_breast_cancer()
feature_names=data.feature_names

## ----------5. User Input Section ------------------
st.subheader("Enter Patient data")
user_input=[]
for feature in feature_names:
  value=st.number_input(feature,value=0.0)
  user_input.append(value)

# convert input to array
input_array=np.array(user_input).reshape(-1,1)

## ----------- 6. Data Preprocessing
scaled_input=scalar.transform(input_array)

## ------------- 7. Prediction Section ----------------
if st.button("Predict"):
  prediction=model.predict(scaled_input)

## ------------- 8.Prediction --------------------------
if prediction[0]==0:
  st.error("Resut:Malignanat(cancer detected)")
else:
  st.sucess("Result: Bengin(No cancer Detected)")
