import streamlit as st
import json
import pickle
import numpy as np

st.set_page_config()

@st.cache_resource
def load_model():
    with open("bangalore_house_model.pickle", 'rb') as fp:
        model = pickle.load(fp)
    
    return model

def predict():
    locs = [0] * len(locations)
    locs[locations.index(loc)] = 1
    inp = np.array([float(sqft), bath, bhk, *locs])
    model = load_model()
    pred = model.predict([inp])
    return pred

locations = []

with open("./columns.json", 'r') as fp:
    js = json.load(fp)
    locations = js['data_columns'][3:]

st.title("House Price Prediction")

loc = st.selectbox("Location", locations)
sqft = st.text_input("Total Sqft.")
bhk = st.number_input("BHK", 0, 10, step=1)
bath = st.number_input("Bathrooms", 0, 10, step=1)

if st.button("Predict!"):
    pred = predict()
    st.text(f"Predicted Price is {pred[0]}")
