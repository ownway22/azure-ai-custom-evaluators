class ClarityEvaluator:
    def __init__(self):
        pass

    def __call__(self, *, answer: str, **kwargs):
        import re

        sentences = re.split(r'(?<=[.!?])\s+', answer.strip())
        num_sentences = len(sentences) if sentences and sentences[0] else 0
        num_words = sum(len(s.split()) for s in sentences)
        avg_sentence_len = num_words / num_sentences if num_sentences else 0

        long_sentences = [s for s in sentences if len(s.split()) > 25]
        long_ratio = len(long_sentences) / num_sentences if num_sentences else 0.0

        return {
            "avg_sentence_length": avg_sentence_len,
            "long_sentence_ratio": long_ratio
        }
