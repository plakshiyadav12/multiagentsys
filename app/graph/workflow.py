from langgraph.graph import StateGraph, START, END

from app.graph.state import ResearchState
from app.graph.nodes import (
    planner_node,
    web_research_node,
    academic_research_node,
    news_research_node,
)


def build_research_graph():

    graph = StateGraph(ResearchState)

    # -------------------------
    # Nodes
    # -------------------------

    graph.add_node(
        "planner",
        planner_node,
    )

    graph.add_node(
        "web_research",
        web_research_node,
    )

    graph.add_node(
        "academic_research",
        academic_research_node,
    )

    graph.add_node(
        "news_research",
        news_research_node,
    )

    # -------------------------
    # Edges
    # -------------------------

    graph.add_edge(
        START,
        "planner",
    )

    # Planner fans out into
    # three research branches.

    graph.add_edge(
        "planner",
        "web_research",
    )

    graph.add_edge(
        "planner",
        "academic_research",
    )

    graph.add_edge(
        "planner",
        "news_research",
    )

    # For now all branches end here.

    graph.add_edge(
        "web_research",
        END,
    )

    graph.add_edge(
        "academic_research",
        END,
    )

    graph.add_edge(
        "news_research",
        END,
    )

    return graph.compile()