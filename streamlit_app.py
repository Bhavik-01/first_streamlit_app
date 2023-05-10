import streamlit
import pandas

streamlit.title("My Mom's New Healthy Dinner")

streamlit.header(' Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Bluebery Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Ranged Egg ')
streamlit.text('🥑🍞 Avocado Toast ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Reading csv file using pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
   
