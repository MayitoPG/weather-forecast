
import logging.config

import streamlit as st

from wf.backend_main import get_data, result
from wf.logging import CONFIG

# Weather Forecast for the next days


logging.config.dictConfig(CONFIG)

logger = logging.getLogger(__name__)


st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
# print(place)
option = st.selectbox("Select data to show", {"Temperature", "Sky"})
# print(option)
st.subheader(f"{option} for {place.title()} ")
days = st.slider("Forecast Days", min_value=1, max_value=5)
try:
    get_data(place, days)
    result(place, days, option)

except KeyError:
    st.subheader("Enter a Location")
if days == 1:
    st.subheader(f"Forecast for {days} day")
else:
    st.subheader(f"Forecast for {days} days")
