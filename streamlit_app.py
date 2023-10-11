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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
# streamlit.text(fruityvice_response.json())
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
  return fruityvice_normalized
   
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
# streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:") 
# streamlit.write('Thanks for adding', add_my_fruit)
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list")
       return my_cur.fetchall()
# add button to load the fruits
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  # my_cur.execute("insert into fruit_load_list values (add_my_fruit)")
  my_data_row = get_fruit_load_list()
  # streamlit.header("The fruit load list contains")
  my_cnx.close()
  streamlit.dataframe(my_data_row)


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
    return "Thanks for adding" + new_fruit
add_my_fruit =  streamlit.text_input('What fruit would you like to add?")
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_func = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_func)



