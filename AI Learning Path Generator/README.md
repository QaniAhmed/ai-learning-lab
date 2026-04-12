# AI Learning Path Generator

## 📌 Overview

AI Learning Path Generator is a project built using LangChain and OpenAI GPT-4o that helps users generate a complete personalized learning plan for any topic.

The system automatically creates:

- A step-by-step learning roadmap
- Recommended resources (courses, websites, books)
- Project ideas (beginner to advanced)
- A structured study plan

---

## 🚀 Features

- 📚 Generates structured learning roadmaps
- 🌐 Suggests high-quality learning resources
- 💻 Provides project ideas from beginner to advanced level
- ⏱ Creates a 10-day study plan
- ⚡ Built using LangChain LCEL (RunnableParallel architecture)

---

## 🧠 How It Works

The project uses LangChain Expression Language (LCEL) to run multiple AI chains in parallel:

- Roadmap Chain → Generates step-by-step learning path
- Resources Chain → Suggests learning materials
- Projects Chain → Generates project ideas
- Study Plan Chain → Creates a structured schedule

All outputs are combined into one final response.

---

## 🛠 Tech Stack

- Python
- LangChain
- OpenAI GPT-4o
- LangChain LCEL
- RunnableParallel
- RunnableSequence

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install langchain langchain-openai
```
