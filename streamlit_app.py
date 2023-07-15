import folium
import streamlit as st

from streamlit_folium import st_folium

takeoff = [45.819626, 11.763332]
landing = [45.806365, 11.785420]

st.set_page_config(page_title="Glide ratio calculator",
    page_icon=":kite:",layout="wide")

val = st.sidebar.slider(
    'Glide ratio',
    0.0, 10.0,8.0)
st.sidebar.metric(label="Glide Ratio",value=f"{val}: 1")

glide_distance =  val * 550
st.sidebar.metric(label="Glide Distance",value=f"{glide_distance} m")

st.sidebar.divider()

wind = st.sidebar.slider(
    label='Head wind',
    min_value=0,
    max_value= 40,
    value=0,
    step=1)
st.sidebar.metric(label="Head Wind",value=f"{wind} m/s")

glide_distance_wind = (10 - wind) * 550

st.sidebar.metric(label="Glide distance with wind",value=f"{glide_distance_wind} m")


m = folium.Map(location=[45.819626, 11.763332], zoom_start=13,tiles = "Stamen Terrain")



folium.Marker(location = takeoff, popup="Stella",
              icon = folium.Icon(color = "green")).add_to(m)

folium.Marker(location = landing, popup="Garden Relais",
              icon = folium.Icon( color = "red")).add_to(m)


folium.Circle(
radius=glide_distance,
location=[45.819626, 11.763332],
color='crimson',
fill=False,).add_to(m)

st_data = st_folium(m, width=1450)
