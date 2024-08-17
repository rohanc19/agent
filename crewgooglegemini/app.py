import streamlit as st
from dotenv import load_dotenv
from crewai import Crew, Process
from agents1 import create_agents
from tasks1 import create_tasks
from tools1 import SerperDevTool

load_dotenv()

st.set_page_config(page_title="AI Trend Analysis", page_icon="🤖", layout="wide")

st.title("🤖 AI Trend Analysis")

topic = st.text_input("Enter a topic for AI trend analysis:", placeholder="e.g., AI in healthcare")

if st.button("Analyze Trends"):
    if topic:
        with st.spinner(f"Analyzing AI trends in {topic}..."):
            try:
                news_researcher, news_writer = create_agents()
                research_task, write_task = create_tasks(topic, news_researcher, news_writer)

                crew = Crew(
                    agents=[news_researcher, news_writer],
                    tasks=[research_task, write_task],
                    process=Process.sequential,
                )

                result = crew.kickoff()

                st.success("Analysis complete!")
                st.subheader("Research Report and Article")
                st.markdown(result)

                # Offer download option for the article
                st.download_button(
                    label="Download Analysis",
                    data=result,
                    file_name="ai-trend-analysis.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a topic for analysis.")

st.sidebar.markdown("## About")
st.sidebar.markdown("This app uses AI to analyze trends in various topics related to artificial intelligence.")
st.sidebar.markdown("Enter a topic in the main panel to get started!")