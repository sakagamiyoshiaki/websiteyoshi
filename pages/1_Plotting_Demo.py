
import time
import numpy as np
import streamlit as st
from streamlit.hello.utils import show_code
from matplotlib import pyplot as plt
import requests
import pandas as pd

key='4c09891a71d24ce289891a71d29ce27f'

station='IPALHO4'
data='20221005'

reqc = requests.get('https://api.weather.com/v2/pws/history/hourly?stationId='+station+'&format=json&units=m&date='+data+'&apiKey='+key)

#Converter em dataframe e salvar em csv
df=pd.DataFrame(reqc.json()['observations']);
df2=pd.json_normalize(df['metric'])

fig, ax = plt.subplots()
ax.plot(2*df2['windspeedAvg']/3.6)

def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)
    st.pyplot(fig)
    
    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

plotting_demo()

show_code(plotting_demo)
