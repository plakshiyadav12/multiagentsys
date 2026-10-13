from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.models.schemas import ResearchPlan

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    
)


planner = llm.with_structured_output(ResearchPlan)


def create_research_plan(question: str) -> ResearchPlan:
    prompt = f"""
You are a research planning agent.

Your job is to break a research question into
specific, independent questions that can be investigated
using external sources.

Research question:
{question}

Create a comprehensive but focused research plan.

Avoid redundant questions.
Each sub-question should investigate a distinct aspect
of the main question.
"""

    return planner.invoke(prompt)