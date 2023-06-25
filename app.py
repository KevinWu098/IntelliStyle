import gCalendar, weather, chatAI

# Test events
# event_summaries = ["Dinner Date"]
# event_summaries = ', '.join(event_summaries)

import gradio as gr

def getOutfit(dummy_argument):
    event_summaries = gCalendar.getCalendarEvents()
    if isinstance(event_summaries, list):
        event_summaries = ", ".join(event_summaries)

    generated_outfit = chatAI.CustomChatGPT(event_summaries)

    return (
        "Your Event(s): \n"
        f'{event_summaries} \n'

        "\n"

        "Suggested Outfit: \n"
        f'{generated_outfit}'
    )

import requests
API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"
headers = {"Authorization": f"Bearer {API_KEY}"}

def classifyClothing(filepath):
    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

    output = query(filepath)

    return output[0]["label"] if output else None

with gr.Blocks() as demo:
    with gr.Tab("Get Outfit(s) Based on Your Schedule"):
        with gr.Row():
            gr.Markdown(
                """
                <h1> <center> IntelliStyle </center> </h1>
                <h3> <center> 
                IntelliStyle is integrated with your Google Calendar, allowing it to suggest optimized outfits for your upcoming day. 
                </br>
                It also takes into account weather conditions, making sure you're looking your best — rain or shine. 
                </center> </h3>
                """
            )

        with gr.Row():
            outputs=gr.Textbox(lines=5, label="Generated Outfit")
        
        with gr.Row():
            btn = gr.Button("Run")
            btn.click(fn=getOutfit, inputs=btn, outputs=outputs)

        with gr.Row():
            gr.Markdown(
                """
                </br>
                <h4 style="text-align:center"> <i><u> Please do not spam the button as errors will occur if you use it too rapidly. </u></i> </h4>
                """
        )
    
    with gr.Tab("Upload Clothing Items"):
        gr.Markdown(
            """
            <h1> <center> Upload Clothes to IntelliStyle </center> </h1>
            <h3> <center> 
            Adding images of your clothing allows Intellistyle to make even better recommendations — tailored just for you. 
            </br>
            Clothing items are best uploaded on their own, preferably on a clean backdrop while <b>not</b> being worn.
            </center> </h3>
            """
        )

        with gr.Row():
            inp = gr.Image(type="filepath")
            out = gr.Textbox(label="What article of clothing we think you uploaded")

        btn = gr.Button("Run")
        btn.click(fn=classifyClothing, inputs=inp, outputs=out)

        with gr.Row():
            gr.Markdown("""<h1><center>Examples ↓</center><h1>""")
        
        import os
        gr.Examples(
            examples=[
                [os.path.join(os.path.dirname(__file__), "example_tshirt.jpg")],
            ],            
            inputs = gr.Image(type="filepath", height=400),
            outputs = gr.Textbox(label="What article of clothing IntelliStyle thinks was uploaded"),
            fn=classifyClothing,
            cache_examples=True,
        )
demo.launch()