from pydantic import BaseModel, Field


class ResearchSubQuestion(BaseModel):
    question: str = Field(
        description="A specific question that should be investigated."
    )

    purpose: str = Field(
        description="Why answering this question is important to the main research question."
    )


class ResearchPlan(BaseModel):
    main_question: str = Field(
        description="The original research question."
    )

    sub_questions: list[ResearchSubQuestion] = Field(
        description="Specific questions that should be researched."
    )

class Source(BaseModel):
    title: str
    url: str
    content: str
    score: float | None = None


class Evidence(BaseModel):
    claim: str
    supporting_text: str
    source_url: str
    confidence: float

class EvidenceBundle(BaseModel):
    evidence: list[Evidence] = Field(
        description="Evidence extracted from the provided research sources."
    )