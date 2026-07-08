"""
Data Analysis Agent - Analyzes CSV/Excel files
"""

import os
from dotenv import load_dotenv
import pandas as pd
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

class DataAnalysisAgent:
    def __init__(self):
        self.conversation_history = []
        self.data = None
        self.data_summary = None
    
    def load_data(self, file_path: str):
        """Load CSV or Excel file"""
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                self.data = pd.read_excel(file_path)
            else:
                return "Error: Only CSV and Excel files supported"
            
            # Generate summary
            self.data_summary = f"""
Dataset Summary:
- Shape: {self.data.shape[0]} rows, {self.data.shape[1]} columns
- Columns: {', '.join(self.data.columns)}
- Data types: {self.data.dtypes.to_dict()}
- Missing values: {self.data.isnull().sum().to_dict()}
- Basic stats: {self.data.describe().to_string()}
"""
            return "Data loaded successfully!"
        except Exception as e:
            return f"Error loading file: {str(e)}"
    
    def analyze(self, question: str):
        """Analyze data and answer question"""
        if self.data is None:
            return "Please load data first"
        
        # Add to history
        self.conversation_history.append({
            "role": "user",
            "content": question
        })
        
        # Create prompt with data context
        system_prompt = f"""You are a data analyst. 
The user has uploaded a dataset with the following information:

{self.data_summary}

Answer questions about the data accurately and provide insights.
Be specific with numbers and statistics."""
        
        # Get Claude's analysis
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=system_prompt,
            messages=self.conversation_history
        )
        
        answer = response.content[0].text
        
        # Add to history
        self.conversation_history.append({
            "role": "assistant",
            "content": answer
        })
        
        return answer


if __name__ == "__main__":
    agent = DataAnalysisAgent()
    
    print("Data Analysis Agent")
    print("=" * 50)
    print("Commands:")
    print("  load <filepath> - Load CSV or Excel file")
    print("  analyze <question> - Ask about the data")
    print("  exit - Quit\n")
    
    while True:
        command = input("Enter command: ").strip()
        
        if command.lower() == 'exit':
            break
        elif command.lower().startswith('load '):
            file_path = command[5:].strip()
            result = agent.load_data(file_path)
            print(result)
        elif command.lower().startswith('analyze '):
            question = command[8:].strip()
            result = agent.analyze(question)
            print(f"Analysis: {result}\n")
        else:
            print("Unknown command")