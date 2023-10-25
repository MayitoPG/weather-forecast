import plotly.express as px
import requests
import streamlit as st
from secret import api_key

# import os
#
# # Access the API key from the environment variable
# api_key = os.environ.get("API_KEY")
#
# if api_key:
#     # Your code here that uses the API key
#     print("API Key:", api_key)
# else:
#     print("API Key not found. Please set the API_KEY environment variable.")


key = api_key()


def get_data(place, days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}"
    response = requests.get(url)
    data = response.json()
    data_needed = data["list"]
    nr_values = 8 * days
    data_needed = data_needed[:nr_values]
    return data_needed


def list_2_images(sky):
    picture_list = []
    for picture in sky:
        picture = picture.lower()
        picture_path = f"images/{picture}.png"
        picture_list.append(picture_path)
    return picture_list


def result(place, days, option):
    data_needed = get_data(place, days)
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] / 10 for dict in data_needed]
        dates = [dict["dt_txt"] for dict in data_needed]
        figure = px.line(
            x=dates, y=temperatures, labels={"x": "Days", "y": "Temperatures"}
        )
        st.plotly_chart(figure)

    if option == "Sky":
        sky = [dict["weather"][0]["main"] for dict in data_needed]
        print(sky)
        picture_list = list_2_images(sky)
        dates = [dict["dt_txt"] for dict in data_needed]
        print(dates)
        st.image(picture_list, width=80, caption=dates)
        figure = px.line(
            x=dates,
            y=sky,
            line_shape="linear",
            labels={"x": "Days", "y": "Sky"},
        )
        st.plotly_chart(figure)


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3))
