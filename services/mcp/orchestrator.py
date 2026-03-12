from services.vision.inference import predict
from services.environment.inference import predict_environment
from services.policy.bandit import ContextualBandit
from services.policy.strategy import StrategyEngine
from services.llm.explain import ExplanationEngine
from database.crud import save_prediction


class MCPOrchestrator:

    def __init__(self):

        actions = [
            "organic_fertilizer",
            "drip_irrigation",
            "shade_cultivation",
            "mulching",
            "direct_soil"
        ]

        self.bandit = ContextualBandit(actions)
        self.strategy_engine = StrategyEngine()
        self.llm = ExplanationEngine()

    def run_pipeline(self, image_path):

        plant, confidence = predict(image_path)

        if plant == "not_medicinal_plant":
            return {
                "plant": plant,
                "confidence": confidence,
                "message": "Uploaded image is not a medicinal plant"
            }

        soil = "loamy"
        temperature = 34
        humidity = 60
        rainfall = 80
        season = "summer"

        suitability = predict_environment(
            plant, soil, temperature, humidity, rainfall, season
        )

        context = {
            "plant": plant,
            "soil": soil,
            "temperature": temperature
        }

        strategy = self.bandit.select_action(context)
        strategy_info = self.strategy_engine.get_strategy(strategy)

        explanation = self.llm.generate(
            plant, suitability, strategy, soil, temperature, rainfall
        )

        prediction_id = save_prediction(
            plant, confidence, soil, temperature,
            rainfall, suitability, strategy, explanation
        )

        return {
            "prediction_id": prediction_id,
            "plant": plant,
            "confidence": confidence,
            "suitability_score": suitability,
            "recommended_strategy": strategy,
            "description": strategy_info["description"],
            "benefit": strategy_info["benefit"],
            "explanation": explanation
        }