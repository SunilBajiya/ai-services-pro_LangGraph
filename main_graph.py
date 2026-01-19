from langgraph.graph import StateGraph
from models.state import WorkflowState
from nodes.planner import planner_node
from nodes.data_fetch import data_fatch_nde
from nodes.validation import validation_node
from nodes.approval import approval_node
from nodes.delivery import delivery_node

def build_graph():
    graph = StateGraph(WorkflowState)
    graph.add_node("planner",planner_node)
    graph.add_node("fetch",data_fatch_nde)
    graph.add_node("validate",validation_node)
    graph.add_node("approve",approval_node)
    graph.add_node("deliver",delivery_node)



    graph.set_entry_point("planner")
    graph.add_edge("planner","fetch")
    graph.add_edge("fetch","validate")
    graph.add_edge("validate","approve")
    graph.add_edge("approve","deliver")


    graph.set_finish_point("deliver")
    return graph.compile()