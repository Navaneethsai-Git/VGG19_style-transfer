# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image

import style

st.title('Deep Learning Style Transfer')

# img = st.sidebar.selectbox(
#     'Select Image',
#     ('amber.jpg', 'cat.png', 'kid.jpg')
# )
uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)


style_name = st.sidebar.selectbox(
    'Select Style',
    ('colour', 'oily', 'tint', 'structure')
)


model= "saved_models/" + style_name + ".pth"
if uploaded_file is not None:
    input_image = uploaded_file
    output_image = "images/output-images/" + style_name + "-" + uploaded_file.name


st.write('### Source image:')
image = Image.open(input_image)
st.image(image, width=400) # image: numpy array

clicked = st.button('Stylize')

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write('### Output image:')
    image = Image.open(output_image)
    st.image(image, width=400)
    
    
    
st.write('Developed by Navaneet')