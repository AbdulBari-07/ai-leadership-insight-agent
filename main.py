from src.pipeline import run_pipeline

if __name__ == '__main__':
    query = input("Enter your question: ")
    result = run_pipeline(query)
    print("\n=== Anser ===\n")
    print(result)