import streamlit as st
import random

# Define some "tricks" and "treats" with links to images or GIFs
tricks = [
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGcwcnYzOHg2bGpub2kweDZmMXNoNHl2YTUwbTVobWNrNnpmdWt3OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DPvq36SD00MihIDc00/giphy.gif"
]

treats = [
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzk1OG5odXM2bDYzYXUwYTRveTJ0a25mYWF1Z3VjeXE5aDZvbTQ1MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OW7jUTtOeQY0g8YBJF/giphy.gif"  # candy GIF
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
