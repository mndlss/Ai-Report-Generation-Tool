# AI Report Generation Tool  

An **AI-powered report generation system** that leverages **LLaMA 3.2 (via Ollama)** to analyze datasets (CSV format) and automatically generate professional, structured reports.  

This project is designed for **energy data analysis** (e.g., streetlight RTU datasets) but can be extended to other domains with minimal modifications.  

---

## 🚀 Features  

- 📊 **CSV Data Processing** → Reads, preprocesses, and embeds datasets into LLM prompts.  
- 🤖 **LLM-Powered Analysis** → Uses LLaMA 3.2 via Ollama for natural language insights.  
- 📑 **Automatic Report Generation** → Produces human-like, structured analytical reports.  
- ⚡ **Modular Design** → Clean folder structure (`data/`, `model/`, `reports/`, `utils/`).  

---

## 📂 Project Structure  

AI-Report-Generation-Tool/
│── data/ # Input CSV datasets
│── model/ # Model client code (LlamaClient class)
│── reports/ # Generated AI reports
│── templates/ # Report templates (optional, e.g., markdown/HTML)
│── utils/ # Helper functions (e.g., formatters, validators)
│── src/
│ ├── main.py # Main entry point
│ ├── llama_client.py # LLaMA client logic
│── requirements.txt # Python dependencies
│── README.md # Project documentation
