import os
from dotenv import load_dotenv
from google import genai
import time
from google.genai.errors import ServerError

load_dotenv()


class GeminiClient:

    def __init__(self):
        api_key = os.getenv("GENAI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

        if not api_key:
            raise ValueError("GENAI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        for attempt in range(3):
            try:

                response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                )

                return response.text

            except ServerError:
                print(f"Attempt {attempt+1} failed. Retrying...")
                time.sleep(2)

        raise RuntimeError("Gemini API unavailable after 3 attempts.")