import streamlit as st
from PIL import Image
import torch
import numpy as np

from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av

st.title("""Детектор мусора по фотографиям пользователей""")
st.text("""Выполнили студенты Бахтин""")

uploaded_file = st.file_uploader("Choose a file")