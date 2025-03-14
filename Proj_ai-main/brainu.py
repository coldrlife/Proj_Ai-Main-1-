import json
from ai_module import AIModule

class Brainu:
    def __init__(self, config_file="brainu.json"):
        self.config = self.load_config(config_file)
        self.ai = AIModule()

    def load_config(self, config_file):
        with open(config_file, "r") as file:
            return json.load(file)

    def run(self):
        print(f"Running {self.config['model_name']}...")
        self.ai.train("training_data")
        result = self.ai.predict("input_data")
        print(result)

# Example usage
if __name__ == "__main__":
    brainu = Brainu()
    brainu.run()