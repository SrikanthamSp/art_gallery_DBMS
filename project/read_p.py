import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_paintings


def read():
    result = view_all_paintings()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Painting_ID', 'Title', 'Description', 'Year', 'Type','Cost','Artist ID','Sold in exhibition ID','Customer ID'])
    #with st.expander("View all Dealers"):
    st.dataframe(df)
    #with st.expander("Dealer Location"):
        #task_df = df['Dealer City'].value_counts().to_frame()
        #task_df = task_df.reset_index()
        #st.dataframe(task_df)
        #p1 = px.pie(task_df, names='index', values='Dealer City')
        #st.plotly_chart(p1)