import gCalendar, chatAI, weather
import gradio as gr
import requests
import config

API_KEY = config.HF_API_KEY
API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"
headers = {"Authorization": f"Bearer {API_KEY}"}

clothing_list = [] # Utilized in chatAI.py for more personalized suggestions

def getOutfit(dummy_btn_argument, gender):
    event_summaries = gCalendar.getCalendarEvents()
    if isinstance(event_summaries, list):
        event_summaries = ", ".join(event_summaries)
    
    weather_details = weather.getWeather()

    generated_outfit = chatAI.outfitReccomendation(event_summaries, ", ".join(clothing_list), weather_details, gender)

    return (
        "Your Event(s): \n"
        f'{event_summaries} \n'

        "\n"

        "Suggested Outfit: \n"
        f'{generated_outfit}'
    )

def classifyClothing(filepath):
    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

    output = query(filepath)

    if output:
        clothing_list.append(f"[{output[0]['label']}]")
        return [output[0]["label"], ", ".join(clothing_list)]
    else:
        return ["Nothing detected", ", ".join(clothing_list)]

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
            gender_selector = gr.Radio(["Male", "Female", "Non-binary"], label="Gender Identity", info="If gender identity is not provided, results may be less fine-tuned.")

        with gr.Row():
            btn = gr.Button("Connect to Google Calendar and Run")
            btn.click(fn=getOutfit, inputs=[btn, gender_selector], outputs=outputs)

        with gr.Row():
            with gr.Accordion(label="Additional Notes", open=False):
                gr.Markdown(
                    """
                    <h4 style="text-align:center"> <i><u> Please do not spam the button as errors will arise. </br> Additionally, errors may occasionally occur even when all user input is correct. If you believe this to be the case, please refresh the page and try using the demo again. </u></i> </h4>
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

        with gr.Row():
            display_clothing_list = gr.Textbox(label="Uploaded Clothes:")

        btn.click(fn=classifyClothing, inputs=inp, outputs=[out, display_clothing_list])

        with gr.Row():
            with gr.Accordion(label="Additional Notes", open=False):
                gr.Markdown(
                    """
                    <h4 style="text-align:center"> <i><u> Please do not spam the button as errors will arise. </br> Additionally, errors may occasionally occur even when all user input is correct. If you believe this to be the case, please refresh the page and try using the demo again. </u></i> </h4>
                    """
                )

        with gr.Row():
            gr.Markdown("""<h1><center>Demo Example ↓</center><h1>""")
        
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