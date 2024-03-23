#    Copyright 2024 lisatwyw Lisa Y.W. Tang
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import folium, geopy
import streamlit as st
from branca.element import Figure

def map_loc( address ):
  '''
  Returns a map plot for a query string address 
  '''
  geolocator = geopy.geocoders.Nominatim(user_agent="3")
  location = geolocator.geocode( address )         
  lx,ly=location.longitude, location.latitude
  #  If you pass coordinates as positional args, please make sure that the order is (latitude, longitude) or (y, x) in Cartesian terms.
  fig = Figure( width=400,height=200)
  a_map = folium.Map(location = [ly,lx], zoom_start = 16)
  
  p  = geopy.point.Point(ly, lx)
  
  gl = geopy.geocoders.Nominatim(user_agent="my_test") # Without the user_agent it raises a ConfigurationError.
  site = gl.reverse(p)
  site_name = site[0]
  folium.Marker( location=[ly, lx], popup='Default popup Marker3',tooltip=site_name).add_to(a_map)
  fig.add_child(a_map)
  
  return fig, a_map, site_name


st.title( 'My first web app' )

f = 'README.md'
mkd = Path( f ).read_text()
st.markdown( mkd )

st.header( 'My favourite places' )
st.markdown("# Top heading")
st.markdown("## Subheading")

default_addr = 'Stanley Park, Vancouver'   
try:
  address = st.text_area( 'Enter name of queried site for forecasts:', value=default_addr )
  fig, a_map, site_name = map_loc(address)
  st_folium( a_map )
except:    
  try:
    fig, a_map, site_name = map_loc(default_addr)
    st_folium( a_map )
  except Exception as e:
    print( e ) 
  
