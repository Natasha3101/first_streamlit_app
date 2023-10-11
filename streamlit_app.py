import streamlit
import pandas
import requests
# import response
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')
streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3  & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
data = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
data = data.set_index('Fruit')
selected_fruits = streamlit.multiselect("Pick some fruits",list(data.index),['Avocado','Banana'])
show_selected = data.loc[selected_fruits]
streamlit.dataframe(show_selected)
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# streamlit.text(fruityvice_response.json())
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
    streamlit.dataframe(fruityvice_normalized)
# streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error()

streamlit.stop()

streamlit.header("Fruity Fruit Advice!")
try:
  add_my_fruit = streamlit.text_input("what fruit would you like to add?")
  if not add_my_fruit:
    
    
    streamlit.write('Thanks for adding', add_my_fruit)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_cur.execute("insert into fruit_load_list values (add_my_fruit)")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)




