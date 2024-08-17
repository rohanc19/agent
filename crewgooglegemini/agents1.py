from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools1 import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def create_agents():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", 
                                 verbose=True,
                                 temperature=0.5,
                                 google_api_key=os.getenv("GOOGLE_API_KEY"))

    tool = SerperDevTool()

    news_researcher = Agent(
        role="Senior Researcher",
        goal="Uncover ground breaking technologies in the given topic",
        verbose=True,
        memory=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of innovation, eager to explore and share information that could change the world."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=True
    )

    news_writer = Agent(
        role="Writer",
        goal="Narrate compelling tech stories about the given topic",
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=False
    )

    return news_researcher, news_writer