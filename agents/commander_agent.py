## AI Digital Twin Command Center
from boto3 import session
from strands import Agent
from strands.models import BedrockModel
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

# For this python program to work we need to have AWS_PROFILE and AWS_DEFAULT_REGION set in .env file
session = boto3.Session(region_name=os.getenv("AWS_REGION"), profile_name=os.getenv("AWS_PROFILE"))

bedrock_model=BedrockModel(
    model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    boto_session=session,
)
commander_agent = Agent(
    model=bedrock_model,
    system_prompt="""
    You are a commander agent that is responsible for the overall direction of the AI Digital Twin Command Center.
    Your job is to help and analyze incidents and explain what should be investigated and what should be ignored.
    For now you dont have access to any tools, but you will in the future.So keep your responses short and concise. """
)

if __name__ == "__main__":
    respose= commander_agent("The checkout service is experiencing high latency what should be investigated?")
    print(respose)