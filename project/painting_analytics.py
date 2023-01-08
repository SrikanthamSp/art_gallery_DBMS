import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_painting_analytics


def painting_analytics():
    result = view_painting_analytics()
    df = pd.DataFrame(result, columns=['Painting ID', 'Title','Cost'])
    #with st.expander("View all Dealers"):
    st.dataframe(df)

