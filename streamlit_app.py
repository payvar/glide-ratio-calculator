import folium
import streamlit as st

from streamlit_folium import st_folium

takeoff = [45.819626, 11.763332]
landing = [45.806365, 11.785420]
takeoff_height = 712
landing_height = 160

st.set_page_config(
    page_title="Glide ratio calculator", page_icon=":kite:", layout="wide"
)

glide_ratio = st.sidebar.slider(
    "Glide ratio", min_value=0.0, max_value=10.0, value=8.0, step=1.0
)
st.sidebar.metric(label="Glide Ratio", value=f"{glide_ratio}: 1")

glide_distance = glide_ratio * (takeoff_height - landing_height)
st.sidebar.metric(label="Glide Distance", value=f"{int(glide_distance)} m")

st.sidebar.divider()

wind = st.sidebar.slider(label="Head wind", min_value=0, max_value=40, value=0, step=1)

st.sidebar.metric(label="Head Wind", value=f"{wind} m/s")

glide_distance_wind = (glide_ratio - wind) * (takeoff_height - landing_height)

st.sidebar.metric(label="Glide distance with wind", value=f"{glide_distance_wind} m")

m = folium.Map(location=[45.819626, 11.763332], zoom_start=13, tiles="Stamen Terrain")

start_popup_text = """
<b>Stella</b><br>
712m<br>
"""
folium.Marker(
    location=takeoff, popup=start_popup_text, icon=folium.Icon(color="green")
).add_to(m)

landing_popup_text = """
<b>Garden Relais</b><br>
160m<br>
"""

folium.Marker(
    location=landing, popup=landing_popup_text, icon=folium.Icon(color="red")
).add_to(m)

folium.Circle(
    radius=glide_distance_wind,
    location=[45.819626, 11.763332],
    color="red",
    fill=False,
).add_to(m)

folium.Circle(
    radius=glide_distance,
    location=[45.819626, 11.763332],
    color="green",
    fill=False,
).add_to(m)


st_data = st_folium(m, width=1450)
