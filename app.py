import streamlit as st
import pandas as pd
from pypdf import PdfReader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# --- 1. Schema ---
class SkillAnalysis(BaseModel):
    skill: str = Field(description="The skill name")
    is_present: str = Field(description="Yes or No")
    needs_development: str = Field(description="Yes or No")

class ResumeAnalysis(BaseModel):
    analysis: List[SkillAnalysis]

# --- 2. Model ---
HF_TOKEN = "HF_TOKEN" 

llm_base = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.1
)
llm = ChatHuggingFace(llm=llm_base)

# --- 3. Logic ---
def analyze_resume(resume_text, job_desc):
    parser = PydanticOutputParser(pydantic_object=ResumeAnalysis)
    

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a strict HR bot. Output ONLY valid JSON. No conversation. No preamble. Match the exact schema provided."),
        ("human", "Resume: {resume_text}\nJD: {job_desc}\n\n{format_instructions}")
    ])
    
    chain = prompt | llm | parser
    return chain.invoke({
        "resume_text": resume_text, 
        "job_desc": job_desc,
        "format_instructions": parser.get_format_instructions()
    })

# --- 4. UI ---
st.set_page_config(page_title="AI Matcher", layout="wide")
st.title("🚀 Skill Gap Analyzer")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
job_description = st.text_area("Paste JD")

if st.button("Analyze Match"):
    if uploaded_file and job_description:
        with st.spinner("Decoding Skills..."):
            try:
                reader = PdfReader(uploaded_file)
                text = "".join([p.extract_text() for p in reader.pages])
                result = analyze_resume(text, job_description)
                
                st.success("Match Found!")
                st.table(pd.DataFrame([item.dict() for item in result.analysis]))
            except Exception as e:
                st.error("Model returned text instead of Table. Please try again in a moment.")
                st.expander("Technical details").write(str(e))
   
