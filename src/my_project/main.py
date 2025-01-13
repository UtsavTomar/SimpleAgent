from my_project.crew import SimpleAgentCrew

def run():

    inputs = {
        "text": "This is a simple example of how to use a GROQ agent. The agent processes text and provides a summary."
    }
    # Kicking off the crew
    result = SimpleAgentCrew.crew().kickoff(inputs=inputs)

    # Save the summary result as a Markdown file
    with open("summary.md", "w") as f:
        f.write(result.raw)
