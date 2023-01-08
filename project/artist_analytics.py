import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_artist_analytics


def artist_analytics():
    result = view_artist_analytics()
    df = pd.DataFrame(result, columns=['Artist ID', 'First Name','Last Name', 'Number of paintings', 'Revenue'])
    #with st.expander("View all Dealers"):
    st.dataframe(df)

