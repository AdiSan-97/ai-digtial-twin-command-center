## AI Digital Twin Command Center
from strands import Agent

commander_agent = Agent(
    system_prompt="""
    You are a commander agent that is responsible for the overall direction of the AI Digital Twin Command Center.
    Your job is to help and analyze incidents and explain what should be investigated and what should be ignored.
    For now you dont have access to any tools, but you will in the future.So keep your responses short and concise. """
)

if __name__ == "__main__":
    respose= commander_agent("The checkout service is experiencing high latency what should be investigated?")
    print(respose)