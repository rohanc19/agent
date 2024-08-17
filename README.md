# AI Trend Analysis with CrewAI

This project uses CrewAI to analyze AI trends on various topics. It leverages Streamlit for the user interface, allowing users to input a topic and receive an AI-generated analysis of trends in that area.

## Project Structure

- `app.py`: Main Streamlit application file
- `agents.py`: Defines AI agents (Senior Researcher and Writer)
- `tasks.py`: Defines tasks for the AI agents
- `tools.py`: Contains custom tools used by the agents (SerperDevTool)

## Prerequisites

- Python 3.7+
- Streamlit
- CrewAI
- dotenv
- langchain_google_genai

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   GOOGLE_API_KEY=your_google_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter a topic in the text input field (e.g., "AI in healthcare").

4. Click the "Analyze Trends" button to start the analysis.

5. Wait for the analysis to complete. The results will be displayed on the page.

6. You can download the analysis as a Markdown file using the "Download Analysis" button.

## Components

### app.py

This is the main Streamlit application file. It sets up the user interface, handles user input, and orchestrates the CrewAI analysis process.

### agents.py

Defines two AI agents:
1. Senior Researcher: Focuses on uncovering groundbreaking technologies in the given topic.
2. Writer: Crafts compelling narratives about the research findings.

Both agents use the Google Generative AI model (Gemini 1.5 Pro) for natural language processing.

### tasks.py

Defines two main tasks:
1. Research Task: Identifies the next big trend in the given topic, including pros, cons, and overall narrative.
2. Writing Task: Composes an insightful article based on the research findings.

### tools.py

Implements the SerperDevTool, which is used by the agents for web searches and information gathering.

## Customization

You can customize the behavior of the AI agents by modifying their roles, goals, and backstories in `agents.py`. Similarly, you can adjust the task descriptions and expected outputs in `tasks.py` to fine-tune the analysis process.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]
