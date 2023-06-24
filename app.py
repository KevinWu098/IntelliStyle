import gCalendar, weather, chatAI

# event_summaries = ["Pickleball match", "Business meeting with executives"]
# event_summaries = ', '.join(event_summaries)

# event_summaries = gCalendar.getCalendarEvents()
# print(event_summaries)
# if isinstance(event_summaries, list):
#     event_summaries = ", ".join(event_summaries)

# suggested_outfit = chatAI.CustomChatGPT(event_summaries)
# print(suggested_outfit)

import gradio as gr

def getOutfit(dummy_argument):
    event_summaries = gCalendar.getCalendarEvents()
    if isinstance(event_summaries, list):
        event_summaries = ", ".join(event_summaries)

    generated_outfit = chatAI.CustomChatGPT(event_summaries)

    return (
        "Your Events: \n"
        f'{event_summaries} \n'

        "\n"

        "Suggested Outfit: \n"
        f'{generated_outfit}'
    )

with gr.Blocks() as demo:
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

demo.launch()