import google.generativeai as palm
import config

palm.configure(api_key=config.BARD_API_KEY)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.8,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}


def outfitRecommendation(events, clothing_list, weather, gender):
    message = """
        You are a pratical personal stylish who gives advice on outfits to wear BASED UPON a user's events in a given day. 
        First, prioritize the events given to you in terms of importance. 
        Then, based on prioritization, create ONE and ONLY ONE outfit for the entire day. 
        Your responses should be short and concise and only contain one outfit.
    """
    message += f"The USER'S events for today are: {events}"
    message += f"The current weather is: {weather}. Adjust THE ONE SINGULAR OUTFIT accordingly."
    message += f"The USER is {gender}. Update suggested outfits accordingly"
    message += f"The USER'S WARDROBE CONSISTS OF THESE ITEMS: {clothing_list}. When possible, prefer to utilize these items, but do so appropriately."    
    message += "Your responses should be short and concise and only contain one outfit."

    response = palm.generate_text(
        **defaults,
        prompt=message
    )
    return(response.result)

# from hugchat import hugchat
# from hugchat.login import Login
# import config

# # Log in to huggingface and grant authorization to huggingchat
# sign = Login(config.HC_EMAIL, config.HC_PASS)
# cookies = sign.login()

# # Save cookies to usercookies/<email>.json
# sign.saveCookies()

# # Create a ChatBot
# chatbot = hugchat.ChatBot(cookies=config.HC_COOKIE)  # or cookie_path="usercookies/<email>.json"

# def outfitReccomendation(events, clothing_list, weather, gender):
#     message = """
#         You are a pratical personal stylish who gives advice on outfits to wear BASED UPON a user's events in a given day. 
#         First, prioritize the events given to you in terms of importance. 
#         Then, based on prioritization, create ONE and ONLY ONE outfit for the entire day. 
#         Your responses should be short and concise and only contain one outfit.
#     """

#     message += f"The current weather is: {weather}. Adjust THE ONE SINGULAR OUTFIT accordingly."
#     message += f"The USER is {gender}. Update suggested outfits accordingly"
#     message += f"The USER'S WARDROBE CONSISTS OF THESE ITEMS: {clothing_list}. When possible, prefer to utilize these items, but do so appropriately."    

#     message += f"The USER'S events for today are: {events}"
    
#     return(chatbot.chat(message))

# import openai
# import config
# openai.api_key = config.openai.api_key
# openai.api_base = config.openai.api_base

# messages = [{"role": "system", 
#              "content": "You are a pratical personal stylish who gives advice on outfits to wear BASED UPON a user's events in a given day. \
#              First, prioritize the events given to you in terms of importance. \
#              Then, based on prioritization, create ONE and ONLY ONE outfit for the entire day. \
#              Your responses should be short and concise. For example: 'Khaki shorts, light t-shirt, comfortable dress shoes' would be an optimal response"
#             }]

# import weather

# messages[0]["content"] += f"The current weather is: {weather.getWeather()}. Adjust THE ONE SINGULAR OUTFIT accordingly."

# def CustomChatGPT(events, clothing_list, gender):
#     messages[0]["content"] += f"The USER' is {gender}. Update suggested outfits accordingly"
#     messages[0]["content"] += f"The USER'S WARDROBE CONSISTS OF THESE ITEMS: {clothing_list}. When possible, prefer to utilize these items, but do so appropriately."
#     messages.append({"role": "user", "content": events})
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",    
#         messages = messages
#     )
#     ChatGPT_reply = response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": ChatGPT_reply})
#     return ChatGPT_reply