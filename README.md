# AI-Skill-Gap-Analyzer
An AI-powered application developed during a 6-week internship at Tips Hindawi to automate resume screening. It uses Llama-3 and RAG logic to extract data from PDF resumes and compare them against Job Descriptions. The tool generates a structured table identifying skill gaps to help candidates align with market requirements.
# Features
• Resume Analysis: Extracts and structures data from PDF resumes using PyPDF.

• AI Comparison: Uses LangChain and Hugging Face (Llama 3) to compare candidate skills against job requirements.

• Actionable Insights: Generates a structured table highlighting missing skills and areas for improvement.

• Web Deployment: Deployed as a functional Web App using Streamlit and ngrok.
# 🛠️Tech Stack

• Python 3.10+: Core programming language.

• Streamlit: For building the interactive web interface.

• LangChain: Orchestrating the LLM workflow and prompting.

• Hugging Face (Llama-3-8B): The brain behind the skill analysis.

• Pydantic: Ensuring structured and consistent JSON output.

• PyPDF: Parsing and extracting text from PDF resumes.

• Pandas: Data manipulation and tabular display.
# App Demo

<img width="1600" height="900" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/7dd0eb55-8d85-4265-b054-796159eeb470" />
<img width="1600" height="900" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/be550811-f35b-4608-9fcd-31ab132add52" />

# Project Structure

📁 AI-Skill-Gap-Analyzer/

## 📁 Project Structure
```text
AI-Skill-Gap-Analyzer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── assets/             # Images and demo video
    ├── demo.mp4
    └── screenshot.png
