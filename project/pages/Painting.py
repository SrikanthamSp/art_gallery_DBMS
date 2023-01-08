# Importing pakages
import streamlit as st
import mysql.connector

from create_p import create
from delete_p import delete
from read_p import read
from update_p import update
from painting_analytics import painting_analytics
from get_exhibition import get_exhibition

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
     )
c = mydb.cursor()
#c.execute("CREATE DATABASE art_gallery")


def main():
    st.title("Painting")
    p_menu = ["Add","View","Update","Remove","Painting analytics","Exhibitions happening"]
    p_choice = st.sidebar.selectbox("Painting", p_menu)

    if p_choice == "Add":
        st.subheader("Enter painting details")
        create()

    elif p_choice == "View":
        st.subheader("Painting details")
        read()

    elif p_choice == "Update":
        st.subheader("Update painting details")
        update()

    elif p_choice == "Remove":
        st.subheader("Remove painting")
        delete()
    
    elif p_choice == "Exhibitions happening":
        get_exhibition()
    
    if p_choice == "Painting analytics":
        st.subheader("Paintings which haven't been sold but displayed in more than one exhibition")
        painting_analytics()

    else:
        st.subheader(" ")


if __name__ == '__main__':
    main()
