# streamlit_app.py
import streamlit as st
import os
import uuid


# Generate a unique key for each download button
def generate_key():
    return str(uuid.uuid4())

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

def show_celebrity_wallpapers(selection):

    if selection == "Celebrity Wallpaper":
        st.header("Celebrity Wallpapers")

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
                    label=f"Download",
                    data=contents,
                    file_name=image,
                    key=download_key
                )

def show_all_wallpapers(selection):
    if selection == "All Wallpaper":
        data_path = "data"
        animate_path = os.path.join(data_path, "animate")
        wallpaper_path = os.path.join(data_path, "wallpaper")

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

# main functions
def main():

# title for extension
    st.title('_:blue[Wally]-Pixel_')
    st.markdown("""
        <style>
        .sidebar-divider {
            background-image: linear-gradient(to right, violet, indigo, skyblue, green, yellow, orange, red);
            height: 3px;
            width: 100%;
            margin-top: -8px;
        }
        </style>
        <div class="sidebar-divider"></div>
        """,
        unsafe_allow_html=True
        )
# sidebar
    st.sidebar.title("_:blue[Wally] Categories_")
    # divider
    st.sidebar.markdown("""
        <style>
        .sidebar-divider {
            background-image: linear-gradient(to right, violet, indigo, skyblue, green, yellow, orange, red);
            height: 3px;
            width: 100%;
            margin-top: -8px;
        }
        </style>
        <div class="sidebar-divider"></div>
        """,
        unsafe_allow_html=True
        )
    

# category button in sidebar
    all_category = st.sidebar.button("All Wallpaper")
    wallpaper_category = st.sidebar.button("Live Wallpaper")
    hd_category = st.sidebar.button("HD Wallpaper")
    celebrity_category = st.sidebar.button("Celebrity Wallpaper")
    

    # wallpaper selections
    if all_category:
        st.empty()
        show_all_wallpapers("All Wallpaper")
    elif wallpaper_category:
        st.empty()
        show_live_wallpapers("Live Wallpaper")
    elif hd_category:
        st.empty()
        show_hd_wallpapers("HD Wallpaper")
    elif celebrity_category:
        st.empty()
        show_celebrity_wallpapers("Celebrity Wallpaper")
    else:
        show_all_wallpapers("All Wallpaper")
        st.empty()
    

if __name__ == '__main__':
    main()
