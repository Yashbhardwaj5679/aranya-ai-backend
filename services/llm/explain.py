class ExplanationEngine:

    def __init__(self):
        # No heavy ML model loading
        pass

    def generate(
        self,
        plant,
        suitability,
        strategy,
        soil,
        temperature,
        rainfall
    ):

        # Interpret suitability score
        if suitability >= 0.8:
            suitability_text = "highly suitable"
        elif suitability >= 0.6:
            suitability_text = "moderately suitable"
        else:
            suitability_text = "less suitable"

        explanation = f"""
The medicinal plant {plant} is {suitability_text} for cultivation in North Haryana.

Environmental conditions:
- Soil type: {soil}
- Temperature: {temperature} °C
- Rainfall: {rainfall} mm

Based on these conditions, the recommended cultivation strategy is {strategy}.

Farmers should maintain proper soil moisture, ensure adequate sunlight, and follow the suggested cultivation method to improve yield.
"""

        return explanation.strip()


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