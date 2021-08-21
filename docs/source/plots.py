import plotly.express as px
import pandas as pd

def density_mapbox(dataframe,lat,lng,z,radius=10,center=dict(lat,lng),zoom,mapbox_style):
    fig = px.density_mapbox()
    fig.show()

