import logging

import plotly.express as px
import requests
import streamlit as st

from wf.config import API_KEY

logger = logging.getLogger(__name__)

# FIXME: move all streamlit code to main.py and return values from backend_main.py
#  test these function mocking the requests.get() call
#  handle errors on the api call and return a proper status code
#  remove all prints and use logger.info() instead


def get_data(place, days=None):
    """
    Get data from the API
    """
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
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
    """
    Display the result
    :param place:
    :param days:
    :param option:
    :return:
    """
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
