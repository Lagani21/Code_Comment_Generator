import openai
from key import GROQ_API_KEY

class Model():
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",  # <- Important
        )

    def ask(self, code):
        question = self.generate_question(code)
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",  # <- FREE Mixtral model
            messages=[{"role": "user", "content": question}],
        )
        answer = response.choices[0].message.content.split("\n")
        return answer

    def generate_question(self, code):
        return "Insert a comment above every line of the following Python code explaining what it does:\n" + code
