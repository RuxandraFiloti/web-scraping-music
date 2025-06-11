import streamlit as st
import plotly.express as px
import pandas
import sqlite3

sql_connection = sqlite3.connect("data.db")
cursor = sql_connection.cursor()

cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall()  #fetches all the rows from the query
date = [item[0] for item in date]  #extracts the first element from each tuple

cursor.execute("SELECT temperature FROM temperatures")
temperature = cursor.fetchall()  #fetches all the rows from the query
temperature = [item[0] for item in temperature]  #extracts the first element from each tuple

#CREATE A PLOT
figure = px.line(x=date, y=temperature,
            labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)



# df = pandas.read_csv("date.txt")

#CREATE A PLOT
# figure = px.line(x=df["date"], y=df["temperature"],
#             labels={"x": "Date", "y": "Temperature (C)"})

# st.plotly_chart(figure)