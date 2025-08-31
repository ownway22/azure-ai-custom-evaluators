from clarity import ClarityEvaluator

evaluator = ClarityEvaluator()

answer_one = (
    "The process has three steps. "
    "First, submit your form online. "
    "Second, wait for the confirmation email. "
    "Finally, attend the scheduled appointment."
)

answer_two = (
    "In order to achieve the objective, it is necessary that the applicant "
    "not only completes the form—which might contain several sections, some "
    "of which are optional but highly recommended depending on the context—"
    "but also ensures that all accompanying documents are provided at the "
    "time of submission, otherwise the process may be delayed or even rejected."
)

result_one = evaluator(answer=answer_one)
result_two = evaluator(answer=answer_two)

print("Answer Evaluation:", result_one) # clear
print("Unclear Answer Evaluation:", result_two) # unclear

