import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import pickle
import streamlit as st
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

