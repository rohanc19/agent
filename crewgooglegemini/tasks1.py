from crewai import Task
from tools1 import SerperDevTool

def create_tasks(topic, news_researcher, news_writer):
    tool = SerperDevTool()

    research_task = Task(
        description=(
            f"Identify the next big trend in {topic}. Focus on identifying pros and cons and the overall narrative. "
            "Your final report should clearly articulate the key points, its market opportunities, and potential risks."
        ),
        expected_output="A comprehensive 3 paragraphs long report on the latest AI trends",
        agent=news_researcher
    )

    write_task = Task(
        description=(
            f"Compose an insightful article on {topic}. "
            "Focus on the latest trends and how it's impacting the industry. "
            "This article should be easy to understand, engaging and positive."
        ),
        expected_output=f"A 4 paragraph article on {topic} advancements formatted as markdown.",
        agent=news_writer
    )

    return research_task, write_task