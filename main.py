import os
import json
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

# Initialize the GenAI client (automatically picks up GEMINI_API_KEY from environment variables)
client = genai.Client()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/explain", sorted_keys=False, methods=["POST"])
def explain_keyword():
    data = request.get_json() or {}
    keyword = data.get("keyword", "").strip()
    
    if not keyword:
        return jsonify({"error": "Please enter a keyword."}), 400

    # System instruction enforces structured JSON output for easy frontend consumption
    prompt = f"Explain the DBMS concept: '{keyword}'"
    system_instruction = (
        "You are a strict DBMS assistant. Provide an explanation for the given keyword. "
        "You MUST respond ONLY with a valid JSON object matching this schema:\n"
        "{\n"
        "  \"explanation\": \"A short, crystal-clear explanation of the concept.\",\n"
        "  \"example_code\": \"A practical, clean SQL statement, query, or schema layout illustrating its exact real-world use case. Do not use markdown wrappers here.\"\n"
        "}"
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Fast and highly optimized free-tier model
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",
                temperature=0.2
            )
        )
        
        # Parse output directly into JSON format to send to client
        result_data = json.loads(response.text)
        return jsonify(result_data)

    except Exception as e:
        return jsonify({"error": f"Failed to fetch explanation. Details: {str(e)}"}), 500

# Vercel needs the app variable exposed
if __name__ == "__main__":
    app.run(debug=True)