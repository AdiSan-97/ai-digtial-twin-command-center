## AI Digital Twin Command Center
from boto3 import session
from strands import Agent
from strands.models import BedrockModel
import boto3
import os
from tools.get_infra_metrify import get_infra_metrify
from strands.session import FileSessionManager, session_manager
from dotenv import load_dotenv
load_dotenv()

# For this python program to work we need to have AWS_PROFILE and AWS_DEFAULT_REGION set in .env file
session = boto3.Session(region_name=os.getenv("AWS_REGION"), profile_name=os.getenv("AWS_PROFILE"))

session_manager= FileSessionManager(
    session_id="incident-1024",
    storage_dir="./sessions"
)

bedrock_model=BedrockModel(
    model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    boto_session=session,
)
commander_agent = Agent(
    model=bedrock_model,
    system_prompt="""
    You are a commander agent that is responsible for the overall direction of the AI Digital Twin Command Center.
    Your job is to help and analyze incidents and explain what should be investigated and what should be ignored.
    You have access to infrastructure tool. Dont use tools when they are not relavent to the incident.
    Use it to analyze the infrastructure metrics and help the user to investigate the incident. """,
    tools=[get_infra_metrify],
    session_manager=session_manager
)




## Does the agent remembers the conversation once its been restarted? (Ans: No, Agent could no longer access the previous conversation.)
if __name__ == "__main__":
    # response=commander_agent(
    #    "Remember this incident: INC-1024 affects the checkout-api service."
    # )
    response=commander_agent(
       "Which service was affected in incident INC-1024?"
       "Answer using previous conversation"
    )