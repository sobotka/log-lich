import streamlit

streamlit.title("Log-Like Camera Encoding LICH")

upload_image = streamlit.sidebar.file_uploader(
    label="", key="Custom Upload Image", type=[".exr", ".hdr"]
)