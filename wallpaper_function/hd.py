import streamlit as st
import os
from wally_pix import generate_key

def show_hd_wallpapers(selection):

    if selection == "HD Wallpaper":
        st.header("HD Wallpapers")

        # Path to the folder containing images
        images_folder = 'data/wallpaper'    

            # List all files in the images folder
        image_files = os.listdir(images_folder)

        # Create a dictionary to store unique keys for download buttons
        download_keys = {}

        # Display images and allow download
        for idx, image in enumerate(image_files):
            image_path = os.path.join(images_folder, image)
            # Display image
            st.image(image_path, use_column_width=True)

            # Generate a unique key for each button
            download_key = generate_key()
            download_keys[image] = download_key

            # Provide download link for each image
            with open(image_path, 'rb') as file:
                contents = file.read()
                st.download_button(
                    label=f"Download {image}",
                    data=contents,
                    file_name=image,
                    key=download_key
                )