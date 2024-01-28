# Import necessary libraries
import streamlit as st
from PIL import Image

# Page title and description
st.title("Image Resizer")
st.write("Upload an image, specify the target size in kilobytes, and download the resized image.")

# File uploader widget for image input
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Input for target size in kilobytes
target_size_kb = st.number_input("Target Size (KB)", min_value=1, step=1)

# Resize image function
def resize_image(image, target_size_kb):
    # Convert target size to bytes
    target_size_bytes = target_size_kb * 1024

    # Open the image using PIL
    img = Image.open(image)

    # Calculate new dimensions
    original_size = len(image.getvalue())
    compression_ratio = target_size_bytes / original_size
    new_width = int(img.width * compression_ratio**0.5)
    new_height = int(img.height * compression_ratio**0.5)

    # Resize the image
    resized_img = img.resize((new_width, new_height))

    return resized_img

# Display resized image if available
if uploaded_file is not None:
    # Resize the image
    resized_image = resize_image(uploaded_file, target_size_kb)

    # Display the resized image
    st.image(resized_image, caption="Resized Image", use_column_width=True)

    # Download button for resized image
    st.download_button(
        label="Download Resized Image",
        data=resized_image.tobytes(),
        file_name="resized_image.jpg",
        mime="image/jpeg"
    )
