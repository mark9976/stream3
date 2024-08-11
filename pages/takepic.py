import streamlit as st
from pyiphone import iPhoneCamera

# Create an instance of the iPhoneCamera class
camera = iPhoneCamera()

# Display the camera feed on screen
st.write(camera.get_feed())

# Take a photo
photo = camera.take_photo()

# Save the photo to disk
with open("photo.jpg", "wb") as f:
    f.write(photo)

# Close the connection to the camera
camera.close()