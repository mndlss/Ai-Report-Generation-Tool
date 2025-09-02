import pandas as pd
import ollama
import os
import json

class LlamaClient:
    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name

    def read_and_prepare_prompt(self, file_path: str, user_prompt: str) -> str:
        """
        Read CSV, convert to JSON string, embed in prompt.
        """
        try:
            df = pd.read_csv(file_path)
            # If too big, truncate
            if len(df) > 30:
                df = df.head(30)

            json_data = df.to_json(orient="records", indent=2)

            full_prompt = f"""
            You are a data analyst working with energy data collected from streetlight RTUs.

            Here is the user input:
            {user_prompt}

            Now analyze the following dataset:
            {json_data}

            Please provide:
            - A summary of the shape, size and duration of dataset. With duration I mean from when to when is the dataset based on and for how many months, year and days.
            - Summary of patterns that you can find the dataset
            - Any anomalies or outliers
            - Mention if cam switch mode affects readings
            - Suggestions for optimization
            - Include the power consupmption at a daily basis
            """

        #     full_prompt = f"""
        #     You are a data analyst working with energy data collected from streetlight RTUs.

            return full_prompt
        except Exception as e:
            print(f"❌ Error preparing prompt: {e}")
            raise

    def generate_response(self, prompt: str) -> str:
        """
        Sends the prompt to the locally running Ollama model.
        """
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response['message']['content']
        except Exception as e:
            print(f"❌ Error generating response from LLaMA: {e}")
            return ""

    def generate_report_from_file(self, file_path: str, user_prompt: str) -> str:
        """
        Full pipeline: read file, create prompt, get LLM response.
        """
        try:
            prompt = self.read_and_prepare_prompt(file_path, user_prompt)
            return self.generate_response(prompt)
        except Exception as e:
            print(f"❌ Report generation failed: {e}")
            return ""