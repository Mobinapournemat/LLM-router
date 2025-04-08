from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from groq import Groq
import argparse


DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except LangDetectException:
        return 'unknown'




CATEGORY_MODEL_MAP = {
    "MidEast-SouthAsian": "mistral-saba-24b",
    "EastAsian": "qwen-2.5-32b",
    "math": "deepseek-r1-distill-qwen-32b",
    "coding": "qwen-2.5-coder-32b",
    "long_context": "meta-llama/llama-4-scout-17b-16e-instruct",
    "default": "llama-3.3-70b-versatile"
}


MID_EAST_SOUTH_ASIAN_LANGS = ['ar', 'fa', 'ur', 'he', 'hi', 'bn', 'ta', 'te', 'ml', 'gu', 'pa']  # Arabic, Farsi, etc.
EAST_ASIAN_LANGS = ['zh-cn', 'zh-tw', 'ja', 'ko', 'th', 'vi', 'ms']  # Chinese, Japanese, etc.


def detect_language(text: str) -> str:
    try:
        return detect(text)
    except LangDetectException:
        return 'unknown'


def classify_prompt(client, user_prompt):
    classification_system_prompt = """
You are a classifier AI that labels prompts into one of the following categories:
- math: for math problem solving, logic, or equations
- coding: for programming or debugging
- long_context: if the user provides a very long prompt or needs extended memory
- default: for everything else

Your response should be one of: math, coding, long_context, default
""".strip()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": classification_system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    category = response.choices[0].message.content.strip().lower()
    return category if category in CATEGORY_MODEL_MAP else "default"

def route_to_model(client, user_prompt):
    lang_code = detect_language(user_prompt)
    
    if lang_code in MID_EAST_SOUTH_ASIAN_LANGS:
        category = "MidEast-SouthAsian"
    elif lang_code in EAST_ASIAN_LANGS:
        category = "EastAsian"
    else:
        category = classify_prompt(client, user_prompt)
    
    model = CATEGORY_MODEL_MAP.get(category, CATEGORY_MODEL_MAP["default"])
    print(f"[Detected language: {lang_code}] → [Category: {category}] → [Model: {model}]")
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.choices[0].message.content


def ai_agent(client, user_prompt):
    return route_to_model(client, user_prompt)


def parse_args():
    parser = argparse.ArgumentParser(description="AI Task Routing Agent")
    parser.add_argument('--api-key', required=True, help='Your Groq API key')
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()
    client = Groq(api_key=args.api_key)
    prompt = input("Enter your prompt: ")
    output = ai_agent(client, prompt)
    print("\nAI Agent Response:\n", output)