import openai
from key import GROQ_API_KEY

class Model():
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )

    def ask(self, code, comment_level):
        question = self.generate_question(code, comment_level)
        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": question}],
        )
        full_answer = response.choices[0].message.content

        # Clean the output
        if "```" in full_answer:
            # Extract between the first and last code block
            full_answer = full_answer.split("```")[1]  # assumes ```code``` block
            full_answer = full_answer.replace("python\n", "").strip()

        # Split into lines
        answer = full_answer.split("\n")
        return answer


    def generate_question(self, code, comment_level):
        if comment_level.startswith("Beginner"):
            instruction = "Explain every line very clearly for a non-coder by inserting a comment above each line. ONLY return the code with comments. Do not write any explanation, headers, or notes."
        elif comment_level.startswith("Intermediate"):
            instruction = "Briefly explain each line by inserting a comment above each line. ONLY return the commented code. No extra text, headers, or notes."
        else:  # Minimal
            instruction = "Insert very short clarifying comments only where necessary, directly into the code. ONLY return the code with comments. No explanations or notes."

        return f"{instruction}\n\nHere is the code:\n{code}"

