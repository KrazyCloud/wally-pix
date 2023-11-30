import streamlit as st
import os

# side bar functions
def show_live_wallpapers(selection):
    if selection == "Live Wallpaper":
        st.header("Live Wallpapers", divider="rainbow")

        # Path to the folder containing images
        data_path = "data"
        animate_path = os.path.join(data_path, "animate")

        if os.path.exists(animate_path):
            animate_files = os.listdir(animate_path)
            video_files = [file for file in animate_files if file.endswith(('.mp4', '.avi', '.mov'))]
            for idx, video_file in enumerate(video_files):
                video_path = os.path.join(animate_path, video_file)
                st.video(video_path)

                # Provide download link for each image with a unique key
                with open(video_path, 'rb') as file:
                    contents = file.read()
                    st.download_button(
                        label=f"Download {video_file}",
                        data=contents,
                        file_name=video_file,
                        key=f"video_{idx}"  # Unique key for each download_button
                    )
