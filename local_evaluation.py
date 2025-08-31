from azure.ai.evaluation import evaluate
from clarity import ClarityEvaluator
from helpfulness import HelpfulnessEvaluator
import os
from dotenv import load_dotenv

load_dotenv()

dataset = "dataset.jsonl"

clarity_eval = ClarityEvaluator()

helpfulness_eval = HelpfulnessEvaluator(
    model_config={
        "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "azure_deployment": os.getenv("MODEL_EVALUATION_DEPLOYMENT_NAME"),
        "api_key": os.getenv("AZURE_AI_KEY")
    }
)

project_endpoint = (os.getenv("AZURE_AI_FOUNDRY_PROJECT_ENDPOINT") or "").strip()

# Build common evaluate() args
eval_kwargs = {
    "data": dataset,
    "evaluators": {
        "clarity": clarity_eval,
        "helpfulness": helpfulness_eval,
    },
    "evaluator_config": {
        "clarity": {
            "column_mapping": {"answer": "${data.response}"}
        },
        "helpfulness": {
            "column_mapping": {"response": "${data.response}"}
        },
    },
    "output_path": "./myevalresults.json",
}

# Only send results to Azure AI Studio if a valid endpoint is provided
if project_endpoint and project_endpoint.lower().startswith("http"):
    try:
        results = evaluate(**eval_kwargs, azure_ai_project=project_endpoint)
    except Exception as e:
        # Fallback to local evaluation only (no remote logging) if Azure project logging fails
        print(f"Warning: Remote logging to Azure AI Studio failed: {e}. Falling back to local results only.")
        results = evaluate(**eval_kwargs)
else:
    # Evaluate locally without remote logging to avoid 404s
    results = evaluate(**eval_kwargs)

print(results)

print("Local evaluation results saved to myevalresults.json")