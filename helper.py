import openai

class Helper:

    def __init__(self, openai_key):
        self.api_key = openai_key



    def respond(self, prompt):
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=prompt,
            max_tokens = 100
        )