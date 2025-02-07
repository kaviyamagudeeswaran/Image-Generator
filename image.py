import os
import openai  # pip install openai


openai.api_key = os.getenv("ADMIN_KEY")
user_prompt = "Enter the prompt:"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)