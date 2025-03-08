from google import genai
from config import api_key

class GenaiManager:

    def __init__(self):
        self.client = genai.Client(api_key=api_key)

    def chat(self, message):
        response = self.client.models.generate_content(
            model='gemini-2.0-flash', contents=message
        )
        return response.text
