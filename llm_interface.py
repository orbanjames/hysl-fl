class LLMInterface:
    def __init__(self, model):
        self.model = model
    def analyze(self, prompt):
        return self.model.generate(prompt)
