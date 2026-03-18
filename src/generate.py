import os
import json
from openai import OpenAI

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def generate_answer(context, query):
    prompt = f"""
You are an AI leadership assistant.

STRICT INSTRUCTIONS:
- Answer ONLY using the context.
- If data missing, say "Not found in documents".
- Be consice and executive-friendly

Context: {context}
Question: {query}

Return JSON ONLY in this format:
{
    "answer": ".....",
    "supporting_points": ["...", "..."],
    "risks": ["..."],
    "confidence": "High/Medium/Low"
}
"""
    
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{"role": "user", "content": prompt}],
        temperature = 0
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {"answer": response.choices[0].message.content}
    