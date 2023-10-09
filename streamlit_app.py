import streamlit
# import pyspark
# # import findspark
# from pyspark.sql import SparkSession
import  pandas as pd

# findspark.init()

# spark = SparkSession.builder.appName("snow01").getOrCreate()

data = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(data)

streamlit.title('My Parents New Healthy Diner')
streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3  & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
