import pandas as pd
import streamlit as st
import plotly.express as px
from database import get_exhibitions_happening

def get_exhibition():
    result = get_exhibitions_happening()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Exhibition ID', 'Exhibition Name', 'Exhibition location', 'Start date','End date'])
    #with st.expander("View all Dealers"):
    st.dataframe(df)