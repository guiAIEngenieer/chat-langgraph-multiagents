from langgraph.graph import StateGraph , START , END
from app.langgraph.nodes import node_router , node_technician , node_accountant , node_marketing , choose_node , State

# Graph definition
graph = StateGraph(State)

# Add the nodes in the graph
graph.add_node("node_router", node_router)
graph.add_node("node_technician", node_technician)
graph.add_node("node_accountant", node_accountant)
graph.add_node("node_marketing", node_marketing)

# Defining edges
graph.add_edge(START, "node_router")
graph.add_conditional_edges("node_router", choose_node)
graph.add_edge("node_technician", END)
graph.add_edge("node_accountant", END)
graph.add_edge("node_marketing", END)

# Compiling the graph
app = graph.compile()