from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class ExplanationEngine:

    def __init__(self):

        model_name = "google/flan-t5-base"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate(
        self,
        plant,
        suitability,
        strategy,
        soil,
        temperature,
        rainfall
    ):

        prompt = f"""
Explain briefly why the medicinal plant {plant} is suitable to grow in North Haryana.

Environmental conditions:
soil: {soil}
temperature: {temperature} C
rainfall: {rainfall} mm

Suitability score: {suitability}

Recommended cultivation strategy: {strategy}

Explain in simple terms for a farmer.
"""

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True
        )

        outputs = self.model.generate(
            **inputs,
            max_length=120
        )

        explanation = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return explanation


if __name__ == "__main__":

    engine = ExplanationEngine()

    text = engine.generate(
        plant="lemongrass",
        suitability=0.92,
        strategy="mulching",
        soil="loamy",
        temperature=34,
        rainfall=80
    )

    print(text)