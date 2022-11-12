import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorite')
streamlit.text('\N{flexed biceps} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{flexed biceps} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{flexed biceps} Hard-Boiled Free-Range Egg')
streamlit.text('\N{flexed biceps} Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
