import gradio as gr
import random

# Define some "tricks" and "treats" with links to images or GIFs
tricks = [
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGcwcnYzOHg2bGpub2kweDZmMXNoNHl2YTUwbTVobWNrNnpmdWt3OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DPvq36SD00MihIDc00/giphy.gif"
]  # spooky ghost


treats = [
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzk1OG5odXM2bDYzYXUwYTRveTJ0a25mYWF1Z3VjeXE5aDZvbTQ1MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OW7jUTtOeQY0g8YBJF/giphy.gif"  # candy GIF
]

# Trick function
def show_trick():
    image_url = random.choice(tricks)
    message = "Boo! You got a trick! 👻"
    return message, image_url

# Treat function
def show_treat():
    image_url = random.choice(treats)
    message = "Yay! You got a treat! 🍬"
    return message, image_url

# Gradio interface
with gr.Blocks() as app:
    with gr.Column():
        gr.Markdown("### 🎃🎃🎃 Trick or Treat 🎃🎃🎃! Hehehehe")
        message = gr.Textbox(label="Message", interactive=False)
        image = gr.Image(label="Your Trick or Treat", interactive=False, height=500, width=500)  # Smaller image size
        with gr.Row():
            trick_button = gr.Button("Trick", elem_id="trick-btn")
            treat_button = gr.Button("Treat", elem_id="treat-btn")

    trick_button.click(show_trick, outputs=[message, image])
    treat_button.click(show_treat, outputs=[message, image])

app.launch(share=True)