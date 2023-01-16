import pandas as pd
import numpy as np
from scipy import optimize
import streamlit as st


st.sidebar.title("オーケストラを奏でよう！")

# Create a slider for the volume of the orchestra
volume = st.slider("Volume", 0.0, 1.0, 0.5)

# Create a dropdown menu for selecting the instrument
instrument = st.selectbox("Instrument", ["Violin", "Trumpet", "Piano"])

# Create a button for starting and stopping the orchestra
play_button = st.button("Play")

# If the play button is clicked, generate the orchestra sound
if play_button:
    # Generate the orchestra sound using NumPy
    sound = np.random.randn(10000) * volume
    st.write(f"Playing {instrument} with volume {volume}")
    st.audio(sound, rate=44100)