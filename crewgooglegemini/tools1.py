from dotenv import load_dotenv
load_dotenv()

import os
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Create an instance of SerperDevTool
serper_tool = SerperDevTool()

# Function to get the tool
def get_serper_tool():
    return serper_tool