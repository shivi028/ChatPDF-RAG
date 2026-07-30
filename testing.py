# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

# print("Available Models:\n")

# for model in client.models.list():
#     print(model.name)

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)