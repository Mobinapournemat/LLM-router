# 🧠 LLM-router

This is a smart AI agent that takes a user prompt, classifies it into a predefined category (e.g., math, coding, long-context reasoning, etc.), and routes it to a specialized large language model (LLM) hosted on Groq's API for a high-quality response.

## 🚀 Features

- 🔍 **Language Detection**: Automatically detects the language of the input prompt to route it to specific models.
- 🧠 **Prompt Classification**: Uses a general-purpose LLM to classify tasks like math, code, and long-context reasoning.
- 🔁 **Dynamic Model Routing**: Sends the prompt to the best-suited model for accurate and specialized generation.

## 🛠️ Models Used

| Category              | Model Name                                      | Strengths                                      |
|----------------------|--------------------------------------------------|------------------------------------------------|
| MidEast-SouthAsian   | `mistral-saba-24b`                              | Farsi, Arabic, Urdu, Hebrew, Indic languages   |
| EastAsian            | `qwen-2.5-32b`                                  | Chinese, Japanese, Korean, Thai, Vietnamese    |
| Math                 | `deepseek-r1-distill-qwen-32b`                  | Math & logical reasoning                       |
| Coding               | `qwen-2.5-coder-32b`                            | Code generation & debugging                    |
| Long Context         | `meta-llama/llama-4-scout-17b-16e-instruct`     | Very long documents (up to 10M context)        |
| Default/Classifier   | `llama-3.3-70b-versatile`                       | Versatile general-purpose model                |


## 📦 Installation

```bash
git clone https://github.com/Mobinapournemat/LLM-router.git
cd LLM-router
pip install -r requirements.txt
