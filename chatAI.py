import openai
import config
openai.api_key = config.openai.api_key
openai.api_base = config.openai.api_base

messages = [{"role": "system", 
             "content": "You are a pratical personal stylish who gives advice on outfits to wear BASED UPON a user's events in a given day. \
             First, prioritize the events given to you in terms of importance. \
             Then, based on prioritization, create ONE and ONLY ONE outfit for the entire day. \
             Your responses should be short and concise. For example: 'Khaki shorts, light t-shirt, comfortable dress shoes' would be an optimal response"
            }]

import weather

messages[0]["content"] += f"The current weather is: {weather.getWeather()}. Adjust THE ONE SINGULAR OUTFIT accordingly."

def CustomChatGPT(user_input, clothing_list, gender):
    messages[0]["content"] += f"The USER' is {gender}. Update suggested outfits accordingly"
    messages[0]["content"] += f"The USER'S WARDROBE CONSISTS OF THESE ITEMS: {clothing_list}. When possible, prefer to utilize these items, but do so appropriately."
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",    
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply