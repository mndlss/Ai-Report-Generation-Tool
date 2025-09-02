import os
from datetime import datetime
from llama_client import LlamaClient
from utils.file_utils import ensure_folder_exists


DATA_FILE = "/Users/palashkarmakar/Desktop/My Files/Palash/Career/Havells/internships/Project/Ai-Report/src/data/EnergyData_30062025_01.csv"
USER_PROMPT = "Generate a structured technical report about this dataset."
REPORTS_FOLDER = "reports"


def main():
    # Initialize LLaMA client
    client = LlamaClient(model_name="llama3.2")

    # Ensure reports folder exists
    ensure_folder_exists(REPORTS_FOLDER)

    # Generate report
    try:
        report = client.generate_report_from_file(DATA_FILE, USER_PROMPT)

        # Save with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = os.path.join(REPORTS_FOLDER, f"report_{timestamp}.txt")

        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"✅ Report generated and saved to {report_file}")

    except Exception as e:
        print(f"❌ Failed to generate report: {e}")


if __name__ == "__main__":
    main()
