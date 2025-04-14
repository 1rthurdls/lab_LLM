import google.generativeai as genai
import os
from mistralai import Mistral
from dotenv import load_dotenv



load_dotenv()
class Provider:
    def __init__(self, name):
        self.name = name.lower()
        self.api_keys = {
            "gemini":  os.getenv("GEMINI_API_KEY"),
            "mistral": os.getenv("MISTRAL_API_KEY")
        }

    def get_api_key(self):
        return self.api_keys.get(self.name)


class ArthurLLM:
    def __init__(self, provider: Provider, question: str):
        self.provider = provider
        self.question = question

    def answer(self):
        if self.provider.name == "gemini":
            api_key = self.provider.get_api_key()
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(self.question)
            return response.text
        if self.provider.name == "mistral":
            api_key = self.provider.get_api_key()
            model = "mistral-small"
            client = Mistral(api_key=api_key)

            messages = [{"role": "user", "content": self.question}]

            response = client.chat.complete(
                model=model,
                messages=messages
            )

            return response.choices[0].message.content

        return "Provider non pris en charge."

    def display_answer(self):
        response = self.answer()
        print(response)

my_provider = Provider("gemini")
test = ArthurLLM(my_provider, "Qui était président des USA en 2000 ?")
test.display_answer()

my_providers = Provider("mistral")
tests = ArthurLLM(my_providers, "Qui était président des USA en 2010 ?")
tests.display_answer()

