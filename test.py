# # Initialize Nominatim geocoder
# import geopandas as gpd
# import streamlit as st
# from geopy.geocoders import Nominatim
# import folium
# from streamlit_folium import folium_static

# # Initialize Nominatim geocoder
# geolocator = Nominatim(user_agent="my_geocoder")

# # Create a Streamlit app
# st.title("Geocoding App")

# # Ask user for input address
# address = st.text_input("Enter an address to geocode:")

# # Geocode the address
# location = geolocator.geocode(address)
# flag=True
# # Display the results
# if location:
#     flag =False
#     # st.write("Latitude:", location.latitude)
    
#     # st.write("Longitude:", location.longitude)
    
#     # Create a folium map centered at the geocoded location
#     map = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

#     # Add a marker for the geocoded location
#     folium.Marker([location.latitude, location.longitude]).add_to(map)

#     # Display the map
#     folium_static(map)
# else:
#     if address :
#         st.write("Location not found.")




# Initialize Nominatim geocoder
import geopandas as gpd
import streamlit as st
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_geocoder")

# Create a Streamlit app
st.title("Geocoding App")

# Ask user for input address
address = st.text_input("Enter an address to geocode:")

# Geocode the address
location = geolocator.geocode(address)
flag=True

# Display the results
if location:
    flag =False
    # st.write("Latitude:", location.latitude)
    
    # st.write("Longitude:", location.longitude)
    
    # Create a folium map centered at the geocoded location
    map = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)

    # Add a marker for the geocoded location
    folium.Marker([location.latitude, location.longitude]).add_to(map)

    # Display the map
    folium_static(map)
    
    # Create a GeoDataFrame containing the geocoded location
    geometry = gpd.points_from_xy([location.longitude], [location.latitude])
    gdf = gpd.GeoDataFrame(geometry=geometry, crs="EPSG:4326")
    
    # Add a button to download the location as a GeoJSON file
    download_button = st.button("Download location as GeoJSON")
    if download_button:
        st.download_button(
            label="Download",
            data=gdf.to_json(),
            file_name="location.geojson",
            mime="application/json",
        )
else:
    if address :
        st.write("Location not found.")


   
