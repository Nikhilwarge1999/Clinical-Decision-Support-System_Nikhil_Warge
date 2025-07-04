from crewai import Crew, Task
from crew_agents import history_agent, diagnosis_agent, treatment_agent
from rag_utils import query_stg

def run_cdss_pipeline(user_input: str, index_path: str):
    # Task 1: Clinical history
    task1 = Task(
        description=f"Summarize relevant clinical history from this input: {user_input}",
        agent=history_agent,
        expected_output="Concise patient history",
    )

    # Task 2: Diagnosis
    task2 = Task(
        description="Based on the clinical history, suggest the most likely diagnosis.",
        agent=diagnosis_agent,
        expected_output="Likely clinical diagnosis",
    )

    crew1 = Crew(
        agents=[history_agent, diagnosis_agent],
        tasks=[task1, task2],
        verbose=True
    )
    crew1.kickoff()

    diagnosis_text = str(task2.output)
    treatment_guideline = query_stg(diagnosis_text, index_path)

    # Task 3: Treatment
    task3 = Task(
        description=f"Suggest treatment for the diagnosis: {diagnosis_text} using this STG: {treatment_guideline}",
        agent=treatment_agent,
        expected_output="Guideline-aligned treatment plan",
    )

    crew2 = Crew(
        agents=[treatment_agent],
        tasks=[task3],
        verbose=True
    )
    crew2.kickoff()

    return {
        "History": str(task1.output),
        "Diagnosis": diagnosis_text,
        "Treatment": str(task3.output),
    }