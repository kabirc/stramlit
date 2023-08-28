print("hello")
import streamlit as st
st.title("Class Participation - 1")
st.header("Salary Data Statistics")
st.subheader("An Analysis of the Wages and Education levels")
st.subheader("***Built by Kabir Chhabra***")
import pandas as pd
salary_data = pd.read_excel('sds.xlsx')
print(salary_data)
st.write(salary_data)
st.line_chart(salary_data)
st.area_chart(salary_data)
