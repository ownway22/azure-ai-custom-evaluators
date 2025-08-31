import json
from promptflow.client import load_flow

class HelpfulnessEvaluator:
    def __init__(self, model_config):
        self._flow = load_flow("helpfulness.prompty", model_config=model_config)

    def __call__(self, *, response: str, **kwargs):
        llm_output = self._flow(response=response)
        try:
            return json.loads(llm_output)
        except json.JSONDecodeError:
            return {"score": None, "reason": llm_output}
