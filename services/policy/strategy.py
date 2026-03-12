class StrategyEngine:
    """
    Maps cultivation strategies to actual recommendations.
    """

    def __init__(self):

        self.strategies = {

            "organic_fertilizer": {
                "description": "Use compost or cow dung manure to enrich soil nutrients.",
                "benefit": "Improves soil fertility and microbial activity."
            },

            "drip_irrigation": {
                "description": "Apply water slowly through drip lines near plant roots.",
                "benefit": "Saves water and improves plant growth."
            },

            "shade_cultivation": {
                "description": "Grow plants under partial shade to reduce heat stress.",
                "benefit": "Protects delicate medicinal plants from extreme sunlight."
            },

            "mulching": {
                "description": "Cover soil with organic material like straw or leaves.",
                "benefit": "Retains soil moisture and prevents weed growth."
            },

            "direct_soil": {
                "description": "Plant directly in natural soil without additional structures.",
                "benefit": "Suitable for hardy plants like neem or bael."
            }
        }

    def get_strategy(self, strategy_name):

        if strategy_name not in self.strategies:
            return {
                "description": "Unknown strategy",
                "benefit": ""
            }

        return self.strategies[strategy_name]

    def list_strategies(self):

        return list(self.strategies.keys())


# -------------------------
# Test the strategy engine
# -------------------------

if __name__ == "__main__":

    engine = StrategyEngine()

    print("Available strategies:\n")
    print(engine.list_strategies())

    print("\nExample strategy:\n")

    s = engine.get_strategy("drip_irrigation")

    print("Description:", s["description"])
    print("Benefit:", s["benefit"])