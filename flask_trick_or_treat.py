import streamlit as st
import random

# Define some "tricks" and "treats" with links to images or GIFs
tricks = [
    "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",  # spooky ghost
    "https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif",  # jump scare
]

treats = [
    "https://media.giphy.com/media/3oz8xIsloV7zOmt81G/giphy.gif",  # cute pumpkin
    "https://media.giphy.com/media/xT9IgIc0lryrxvqVGM/giphy.gif",  # candy GIF
]

# App title
st.title("🎃 Trick or Treat! Choose wisely!")

# Display message and image based on selection
if st.button("👻 Trick"):
    image_url = random.choice(tricks)
    st.write("Boo! You got a trick!")
    st.image(image_url, width=300)

elif st.button("🍬 Treat"):
    image_url = random.choice(treats)
    st.write("Yay! You got a treat!")
    st.image(image_url, width=300)
