import os 
import openai 
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
class OpenaiClient:
    def __init__(self, model_name = "gpt-4o-mini"):
        self.model_name = model_name
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    
    def readAndPreparePrompt(self, filePath: str, userPrompt: str) -> str:
        """
        
        Reads a csv or excel file and format it into a textual prompt

        """

        try:
            if filePath.endswith(".csv"):
                df = pd.read_csv(filePath)
            elif filePath.endswith((".xls", ".xlsx")):
                df = pd.read_excel(filePath)
            else:
                raise ValueError("Unsupported file format. Please enter a .xls, .xlsx or .csv file.")

            preview = df.head(20).to_string(index=False)        
            fullPrompt = f"""You are an AI assistant that helps with writing technical reports based on the tabular data you get.

            Below is the extracted data from the file:
            {preview}

            User's Instructions are: {userPrompt}

            Generate a concise, structured techincal report summarizing key findings, observations and patterns in the data
            Avoid repitions and aim for clarity and insights into the dataset.
            """
        except Exception as e:
            raise ValueError(f"Error reading or preparing dtaa: {e}")
        
    def generateResponse(self, prompt: str) -> str:
        """
        send prompt to the llm and return the response
        """

        try:
            response = openai.chat.completions.create(
                model = self.model_name,
                messsages = [
                    {"role": "system", "content": "You are a technical assistant skilled at analyzing data and writing professional reports."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5
            )
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            raise ValueError(f"Error generating response: {e}")
        
    def generateResponseFromFile(self, filePath: str, userPrompt: str) -> str:
        """
        read the file, prepare the prompt and get the response from the llm
        """

        prompt = self.readAndPreparePrompt(filePath, userPrompt)
        return self.generateResponse(prompt)