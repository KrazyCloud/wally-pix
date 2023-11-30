import streamlit as st
import os
import uuid
import base64

def show_all_wallpapers(selection):
    if selection == "All Wallpaper":
        data_path = "data"
        animate_path = os.path.join(data_path, "animate")
        wallpaper_path = os.path.join(data_path, "wallpaper")
        celebrity_path = os.path.join(data_path, "celebrity")

        if os.path.exists(wallpaper_path):
            wallpaper_files = os.listdir(wallpaper_path)
            image_files = [file for file in wallpaper_files if file.endswith(('.jpg', '.png', '.jpeg'))]
            for image_file in image_files:
                image_path = os.path.join(wallpaper_path, image_file)
                st.image(image_path)

                # Provide download link for each image
                with open(image_path, 'rb') as file:
                    contents = file.read()
                    # Generate a unique key based on the filename and a unique identifier
                    download_key = f"image_{image_file}_{str(uuid.uuid4())}"
                    st.download_button(
                        label=f"Download {image_file}",
                        data=contents,
                        file_name=image_file,
                        key=download_key
                    )

        if os.path.exists(animate_path):
            animate_files = os.listdir(animate_path)
            video_files = [file for file in animate_files if file.endswith(('.mp4', '.avi', '.mov'))]
            for video_file in video_files:
                video_path = os.path.join(animate_path, video_file)
                st.video(video_path)
                # Provide download link for each image
                with open(video_path, 'rb') as file:
                    contents = file.read()
                    # Generate a unique key based on the filename and a unique identifier
                    download_key = f"video_{video_file}_{str(uuid.uuid4())}"
                    st.download_button(
                        label=f"Download {video_file}",
                        data=contents,
                        file_name=video_file,
                        key=download_key
                    )
        
        if os.path.exists(celebrity_path):
            wallpaper_files = os.listdir(celebrity_path)
            image_files = [file for file in wallpaper_files if file.endswith(('.jpg', '.png', '.jpeg','.webp'))]
            for image_file in image_files:
                image_path = os.path.join(celebrity_path, image_file)
                st.image(image_path)

                # Provide download link for each image
                with open(image_path, 'rb') as file:
                    contents = file.read()
                    # Generate a unique key based on the filename and a unique identifier
                    download_key = f"image_{image_file}_{str(uuid.uuid4())}"
                    st.download_button(
                        label=f"Download \U0001F4E5",
                        data=contents,
                        file_name=image_file,
                        key=download_key
                    )
                    