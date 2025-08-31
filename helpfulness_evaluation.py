from helpfulness import HelpfulnessEvaluator
import os
from dotenv import load_dotenv

load_dotenv()

model_config = {
    "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
    "azure_deployment": os.getenv("MODEL_EVALUATION_DEPLOYMENT_NAME"),
    "api_key": os.getenv("AZURE_AI_KEY")
}

evaluator = HelpfulnessEvaluator(model_config)

answer_one = (
    "To reset your password, go to the login page, click 'Forgot Password', "
    "and follow the instructions sent to your registered email. "
    "If you don't receive an email, check your spam folder or contact support."
)

answer_two = "I don't know. Maybe try something else."

result_one = evaluator(response=answer_one)
result_two = evaluator(response=answer_two)

print("Helpful Answer Evaluation:", result_one)
print("Unhelpful Answer Evaluation:", result_two)
