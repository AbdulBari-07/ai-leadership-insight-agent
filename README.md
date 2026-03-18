# ai-leadership-insight-agent
AI powered leadership assistant to answer strategic questions from company documents

## Approach
## Architecture

User Query
-> Embedding
-> Vector Search (FAISS)
-> Top-K Retrieval
-> LLM (context-aware generation)
-> Structured Output


## Set up instructions

1. Clone the repository
2. Install dependencies from requirements.txt
3. Set API Key (with Export cmd)
4. Add documents in data/sample_docs
5. Run the agent

## Run the Project
'''bash
export OPENAI_API_KEY = input_key_here
python3 main.py

## Evaluation
A sample evaluation pipeline is included to test system performance 