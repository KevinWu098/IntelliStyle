# IntelliStyle

A personal stylist that utilizes your Google Calendar events, upcoming weather, and your own clothes to offer personalized, quality outfits.

<p align="center">
  <img width=300 src="https://github.com/KevinWu098/IntelliStyle/assets/100006999/6d59c957-1ac6-45d2-a969-d45f314fff18" alt="...maybe this wasn't built for programmers"
</p>

## Introduction
Inspired by [this wonderful Youtube video](https://www.youtube.com/watch?v=RlzWluuBhVQ&ab_channel=AdilKhadri), IntelliStyle is a "lite" demo that aims to explore how a personal stylist might be implemented and function through the use of AI tools such as Google's Bard (text-to-text generation) and Microsoft's Resnet50 (image-to-text generation)

Whether it's a critical business meeting with shareholders or a snowstorm you didn't realize was on its way, IntelliStyle aims to prevent wardrobe mishaps by analyzing your upcoming events, the weather, and even clothing that you've uploaded to make sure you're dressed for the occasion. 

For those with busy mornings (or are always rushing), IntelliStyle is a personal tailor that'll give you some peace of mind while figuring out what to wear.

## Features
- Integrates with Google Calendar to retrieve your events for the day
- Outfit suggestions based on calendar events, the weather, and uploaded clothing.
- Upload your own clothing to get more personalized suggestions.

<p align="center">
  <img width="800" alt="Outfit Suggestion" src="https://github.com/KevinWu098/IntelliStyle/assets/100006999/693da423-f9fc-4781-8df8-cbf9a90e31cb">
</p>

<p align="center">
  <img width="800" alt="Clothing Classification" src="https://github.com/KevinWu098/IntelliStyle/assets/100006999/24c080fc-72a5-4661-a9c7-3baddfb7a70d">
</p>

## Running IntelliStyle
Access a live demo of SquishCV hosted on HuggingFace: [IntelliStyle](https://huggingface.co/spaces/hamlegs/IntelliStyle)

## Built With:
- Gradio
- Google Cloud, Google Calendar API, Google's Bard API (outfit suggestions), Microsoft's Resnet50 model (clothing classification), Open-Meteo API (weather)
- Great admiration for the [original inspiration](https://www.youtube.com/watch?v=RlzWluuBhVQ&ab_channel=AdilKhadri)

## Future Plans/Considerations
- Unfortunately, hosting on Huggingface.co presents some challenges making sure that the Google Calendar API / Google Cloud will play nice. I'd say that 95% of the functionality is retained, but this is definitely something I want to pursue and make work!
  - > An option that I'd like to pursue would be to deploy IntelliStyle onto a Flask server or some other lightweight deployment option!
- Currently, IntelliStyle leverages Google's Bard API and Microsoft's Resnet50 model to perform its critical functions. However, with the exception of some light prompting for Bard, both of these models are basically "straight out-of-the-box." Moving forward, I'd like to refine their capabilities by making sure their responses are more tailored to selecting and classfying clothing.
