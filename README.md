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
├── data/
│   └── sample_data.csv        # Example input dataset
│
├── model/
│   └── llama_client.py        # LLaMA client logic (model interface)
│
├── reports/
│   └── report_sample.md       # Example generated AI report
│
├── templates/
│   └── template.md            # Example report template (Markdown)
│
├── utils/
│   └── formatter.py           # Helper functions (e.g., text formatting)
│
├── src/
│   ├── main.py                # Main entry point for running the tool
│   └── pipeline.py            # Orchestration logic (optional, future expansion)
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
