from app.agents.planner import create_research_plan
from app.agents.researcher import research_subquestion
from app.agents.academic import research_academic
from app.agents.news import research_news

from app.graph.state import ResearchState


def planner_node(state: ResearchState) -> dict:
    """
    Create a research plan from the user's question.
    """

    question = state["question"]

    plan = create_research_plan(question)

    return {
        "plan": plan.model_dump(),
        "iteration": 0,
    }


def web_research_node(state: ResearchState) -> dict:
    """
    Run web research for every sub-question.
    """

    plan = state["plan"]

    results = []

    for sub_question in plan["sub_questions"]:

        question = sub_question["question"]

        print(
            f"\n🌐 Web research: {question}"
        )

        result = research_subquestion(
            question=question,
            max_results=3,
            max_evidence_sources=2,
        )

        results.append(result)

    return {
        "web_results": results,
    }


def academic_research_node(state: ResearchState) -> dict:
    """
    Run academic research for every sub-question.
    """

    plan = state["plan"]

    results = []

    for sub_question in plan["sub_questions"]:

        question = sub_question["question"]

        print(
            f"\n📚 Academic research: {question}"
        )

        result = research_academic(
            question=question,
            max_results=3,
            max_evidence_sources=2,
        )

        results.append(result)

    return {
        "academic_results": results,
    }


def news_research_node(state: ResearchState) -> dict:
    """
    Run news research for every sub-question.
    """

    plan = state["plan"]

    results = []

    for sub_question in plan["sub_questions"]:

        question = sub_question["question"]

        print(
            f"\n📰 News research: {question}"
        )

        result = research_news(
            question=question,
            max_results=3,
            max_evidence_sources=2,
        )

        results.append(result)

    return {
        "news_results": results,
    }