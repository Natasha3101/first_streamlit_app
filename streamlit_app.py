import streamlit
# import pyspark
# # import findspark
# from pyspark.sql import SparkSession
import pandas

# findspark.init()
data = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

data = data.set_index('Fruit')
# multi-select
streamlit.multiselect("Pick some fruits",list(data.index))

streamlit.dataframe(data)
# spark = SparkSession.builder.appName("snow01").getOrCreate()
streamlit.title('My Parents New Healthy Diner')
streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3  & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
