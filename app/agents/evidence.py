from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.models.schemas import EvidenceBundle

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0,
)

evidence_extractor = llm.with_structured_output(
    EvidenceBundle
)


def extract_evidence(
    question: str,
    sources: list[dict],
) -> EvidenceBundle:
    """
    Extract evidence from multiple sources
    in a single LLM call.
    """

    source_text = ""

    for i, source in enumerate(sources, start=1):

        source_text += f"""
SOURCE {i}

Title:
{source.get("title", "")}

URL:
{source.get("url", "")}

Content:
{source.get("content", "")}

Source type:
{source.get("source_type", "web")}

-------------------------
"""

    prompt = f"""
You are an evidence extraction agent.

Research question:
{question}

Below are multiple research sources.

{source_text}

Your task is to identify the strongest evidence
from these sources that helps answer the research question.

For each useful piece of evidence:

1. State the specific claim.
2. Quote or closely reproduce the supporting information
   from the source.
3. Provide the source URL.
4. Give a confidence score from 0 to 1.

Important rules:

- Do NOT invent information.
- Do NOT combine unrelated sources into one claim.
- Each claim must be supported by its cited source.
- Prefer concrete facts, statistics, findings, and
  clearly stated conclusions.
- Ignore sources that do not provide useful evidence.
- If sources disagree, preserve the disagreement rather
  than forcing a conclusion.
"""

    return evidence_extractor.invoke(prompt)