import streamlit
# import pyspark
# # import findspark
# from pyspark.sql import SparkSession
import pandas

import snowflake.connector


# findspark.init()
data = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

data = data.set_index('Fruit')

# multi-select
selected_fruits = streamlit.multiselect("Pick some fruits",list(data.index))

show_selected = data.loc[selected_fruits]
streamlit.dataframe(show_selected)
# spark = SparkSession.builder.appName("snow01").getOrCreate()
streamlit.title('My Parents New Healthy Diner')
streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3  & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
