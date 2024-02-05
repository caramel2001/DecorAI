import base64
import requests
import os
import json
import io
from dotenv import load_dotenv
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
def get_recommendations(image, user_pref):
    api_key = os.getenv("OPENAI_API_KEY")

    if isinstance(image, str):
        image = Image.open(image)
    
    # Convert PIL Image to bytes
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")  # or "JPEG", depending on your image format
    image_bytes = buffered.getvalue()

    # Encode in base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')


    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Payload for the request
    payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "system",
      "content": "You are a highly skilled interior designer and prompt engineer with a keen eye for detail. Your expertise lies in analyzing images of rooms, identifying areas that can be enhanced, and recommending products to improve the overall aesthetic and functionality of the space. Your analysis is thorough, considering each section and wall of the room meticulously to ensure no detail is overlooked."
    },
    {
      "role": "user",
      "content": [{
        "type": "text",
        "text": f"# CONTEXT #\n As an interior designer, you are tasked with providing ideas and product recommendations to enhance rooms based on images provided by users.\n\n# OBJECTIVE #\nAnalyze the provided image of a room. Examine the space section by section and wall by wall, meticulously identifying opportunities for improvement. Suggest 4 products that can enhance the room's appearance and functionality, including specific measurements and materials for each product also keep in mind user preferences {user_pref}. Focus on creating a  appealing environment . If the room is empty then recommend the essentials for the particular room . provide a prompt which describes the products properly with positions measurements and all the necessary information so that a fill anything model can add it in , include coordinates and positions or any other way so that i can generate mask so that i can inpaint the image  So the most important thing is generate a prompt that can allow a stable diffusion model to generate an image with the necessary products and materials ensure the prompt uses simple words and is only 80 tokens long please generate a efficent prompt or you will get fired from your job.  \n\n# PROMPT #\n"
      }]
    },
    {
      "role": "user",
      "content": [{
        "type": "image_url",
        "image_url": {
          "url": f"data:image/jpg;base64,{base64_image}"
        }
      }]
    }
  ],
  "max_tokens": 100
}



    # Send the request
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response = response.json()
    print(response)

    prompt = response['choices'][0]['message']['content']
    print(prompt)
    return prompt

# Load user preferences from a file
with open('survey_results.json', 'r') as f:
    user_pref = json.load(f)

# Path to your image
image_path = "images/empty_room.png"

# Send the design request
response = get_recommendations(image_path, user_pref)
print(response)
# Handle the response
# ... (Your code for handling the response)
