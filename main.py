# streamlit_app.py
import streamlit as st
import uuid
from wallpaper_function import all, animated, celebrity, hd

# Generate a unique key for each download button
def generate_key():
    return str(uuid.uuid4())

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
        all.show_all_wallpapers("All Wallpaper")
    elif wallpaper_category:
        st.empty()
        animated.show_live_wallpapers("Live Wallpaper")
    elif hd_category:
        st.empty()
        hd.show_hd_wallpapers("HD Wallpaper")
    elif celebrity_category:
        st.empty()
        celebrity.show_celebrity_wallpapers("Celebrity Wallpaper")
    else:
        all.show_all_wallpapers("All Wallpaper")
        st.empty()
    

if __name__ == '__main__':
    main()
