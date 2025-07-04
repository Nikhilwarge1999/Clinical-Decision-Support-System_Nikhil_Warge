import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()  # Load GROQ_API_KEY from .env
llm=ChatGroq(model_name="groq/llama3-70b-8192",
             api_key=os.getenv("GROQ_API_KEY")
)


history_agent = Agent(
    name="HistoryAgent",
    role="Clinical History Analyzer",
    goal="Extract key patient history from symptoms.",
    backstory="You help doctors by summarizing relevant clinical history from raw input.",
    verbose=True,
    llm=llm
)

diagnosis_agent = Agent(
    name="DiagnosisAgent",
    role="Clinical Diagnostician",
    goal="Suggest potential diagnoses based on clinical history.",
    backstory="You analyze patient history and apply diagnostic logic.",
    verbose=True,
    llm=llm
)

treatment_agent = Agent(
    name="TreatmentAgent",
    role="Treatment Planner",
    goal="Provide guideline-aligned treatment using Gujarat STG.",
    backstory="You apply treatment standards from Gujarat STG to patient cases.",
    verbose=True,
    llm=llm
)