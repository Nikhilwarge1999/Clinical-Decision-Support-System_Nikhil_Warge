# Clinical-Decision-Support-System_Nikhil_Warge

# 🧠 Clinical Decision Support System (CDSS) – Agentic AI with Ayurveda + Groq

**Playing with coding is fun when you understand it!**

This project is an **Agentic AI-powered Clinical Decision Support System (CDSS)** built using the **CrewAI framework** with a focus on **Ayurveda-based diagnosis and treatment recommendations**. It integrates **Groq API** (LLaMA 3), **FAISS vector search**, and **Streamlit** to create a fast, responsive, and intelligent system for clinical decision-making.

---

## 🚀 Features

- 🧑‍⚕️ **HistoryAgent** – Extracts and summarizes patient history  
- 🔍 **DiagnosisAgent** – Performs symptom-based diagnosis using LLM reasoning  
- 💊 **TreatmentAgent** – Recommends Ayurvedic treatment plans  
- 📁 **User File Upload** – Add your own medical data (PDF, TXT, CSV)  
- ⚡ **Real-time Inference** – Powered by Groq API with LLaMA 3  
- 🧠 **Embedding** – Uses `all-MiniLM-L6-v2` for text embedding  
- 🔎 **Semantic Search** – FAISS vector store for fast retrieval  
- 🖥️ **Streamlit UI** – Interactive, simple, and clean

---

## 🌿 Why Ayurveda?

This system integrates **traditional Ayurvedic knowledge** with modern AI, aiming to offer holistic, personalized care through intelligent clinical reasoning.

---

## 🧰 Tech Stack

| Component         | Tool / Library                        |
|------------------|----------------------------------------|
| LLM Inference     | [Groq API](https://console.groq.com/) + LLaMA 3 |
| Agent Framework   | [CrewAI](https://github.com/joaomdmoura/crewai) |
| Vector Store      | FAISS                                 |
| Embeddings        | `sentence-transformers/all-MiniLM-L6-v2` |
| UI Framework      | Streamlit                             |
| Orchestration     | LangChain                             |
| Data Input        | PDF, TXT, CSV                         |

---

## 📂 Folder Structure
│
├── main.py # Entry point to start the app
├── chat_App.py # Streamlit chatbot UI interface
├── Chat_memory.py # Session-based memory handling
├── Crew_agent.py # HistoryAgent, DiagnosisAgent, TreatmentAgent
├── rag_utility.py # RAG logic (embedding, retrieval)
├── requirements.txt # Project dependencies
└── README.md # Project overview



