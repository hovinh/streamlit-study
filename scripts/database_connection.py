import streamlit as st

conn = st.connection("my_database")
df = conn.query("select * from mydb")
st.dataframe(df)