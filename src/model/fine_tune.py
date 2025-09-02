import json
import os 
from openai import OpenAI

class FineTuner:
    def __init__(self):
        """
        Initalize the OpenAI client for fine-tuning tasks.
        Requires OPENAI_API_KEY to be set in teh environment.
        """

        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if not self.client.api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

    def prepareTuningData(self, input_data: list, output_data: list, output_file: str):
        """
        Prepares data for supervised fine-tuning of GPT models (eg, gpt-4o-mini),
        The format is JSONL, with each line being a converstaion.

        Args:
            input_data (list): list of imput prompts (user queries or structured data),
            output_data (list): list of desired model outputs (example completeions).
            output_file (str): path to save the JSONL dataset.
        """

        if len(input_data) != len(output_data):
            raise ValueError("Input and output dtaa lists must have teh same length")
        
        tuning_examples = []
        for i in range(len(input_data)):
            example = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": input_data[i]},
                    {"role": "assistant", "content": output_data[i]},
                ]
            }
            tuning_examples.append(example)

        with open(output_file, "w", encoding="utf-8") as f:
            for entry in tuning_examples:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        print(f"Tuning dataset prepared and saved to {output_file}")

    def upload_dataset(self, file_path: str) -> str:
        """
        Uploads the prepared JSONL dataset to OpenAI.

        Args:
            file_path (str): Path to the dataset file.

        Returns:
            str: The file ID assigned by OpenAI.
        """
        try:
            with open(file_path, "rb") as f:
                uploaded_file = self.client.files.create(file=f, purpose="fine-tune")
            print(f"Dataset uploaded successfully. File ID: {uploaded_file.id}")
            return uploaded_file.id
        except Exception as e:
            raise ValueError(f"Error uploading dataset: {e}")

    def trigger_fine_tuning(self, training_file_id: str, base_model: str = "gpt-4o-mini") -> str:
        """
        Starts a fine-tuning job with the given dataset.

        Args:
            training_file_id (str): File ID of the uploaded dataset.
            base_model (str): Base model to fine-tune (default: gpt-4o-mini).

        Returns:
            str: The fine-tuning job ID.
        """
        try:
            job = self.client.fine_tuning.jobs.create(
                training_file=training_file_id,
                model=base_model
            )
            print(f"Fine-tuning job started. Job ID: {job.id}")
            return job.id
        except Exception as e:
            raise ValueError(f"Error starting fine-tuning job: {e}")

    def check_job_status(self, job_id: str):
        """
        Checks the status of a fine-tuning job.

        Args:
            job_id (str): The fine-tuning job ID.

        Returns:
            dict: Job details including status.
        """
        try:
            job_status = self.client.fine_tuning.jobs.retrieve(job_id)
            return job_status
        except Exception as e:
            raise ValueError(f"Error retrieving job status: {e}")