test_cases = [
    {
        "question": "What is the revenue trend?",
        "expected_keywords": ["growth", "increase"]
    },
    {
        "question": "What risks were mentioned?",
        "expected_keywords": ["risk", "decline", "challenge"]
    }
]

def evaluate(pipeline_fn):
    results = []
    for test in test_cases:
        output = pipeline_fn(test["question"])
        score = 0
        for word in test["expected_keywords"]:
            if word.lower() in str(output).lower():
                score += 1
        results.append({
            "question": test["question"], "score": score/len(test["expected_keywords"])
            })
    return results