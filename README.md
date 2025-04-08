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
```

## 🧪 Usage

### 1. **Run the Agent**

To run the agent, use the following command. You'll need access to Groq's API to pass it as an argument.

```bash
python3 llm_router.py --api-key YOUR_API_KEY_HERE
```

After running the agent, you will be prompted to enter your task. The agent will classify the task and route it to the appropriate model and return the results to you.

## 🧑‍💻 Example Demos
### Example 1: **Farsi Input**

**Input:**
```text
سلام. اسم شما چیه؟
```
**Output:**
```text
[Detected language: fa] → [Category: MidEast-SouthAsian] → [Model: mistral-saba-24b]

AI Agent Response:
من  یک متن هوشمندم و نام خاصی ندارم ،تو میتوانی هر اسمی که خواستی صدا بزن من را، لطفا سوالت رو از من بپرس تا جواب دهم.
```

### Example 2: **Coding Task**

**Input:**
```text
write a python function to generate 10 random samples from a Bernoulli distribution with parameter p = 0.2
```
**Output:**
```text
[Detected language: en] → [Category: coding] → [Model: qwen-2.5-coder-32b]

AI Agent Response:
 Certainly! You can use the numpy library to generate random samples from a Bernoulli distribution. Here's a Python function that generates 10 random samples with a parameter p = 0.2:

python
import numpy as np

def generate_bernoulli_samples(n_samples=10, p=0.2):
    samples = np.random.binomial(n=1, p=p, size=n_samples)
    return samples

# Example usage:
samples = generate_bernoulli_samples()
print(samples)


In this function:
- np.random.binomial is used to generate random samples. The n=1 parameter specifies that each sample is a Bernoulli trial (0 or 1).
- p=0.2 is the probability of success (getting a 1) in each trial.
- size=n_samples specifies the number of samples to generate, which is 10 in this case.

You can run this function, and it will print out 10 random samples from the specified Bernoulli distribution.

```



