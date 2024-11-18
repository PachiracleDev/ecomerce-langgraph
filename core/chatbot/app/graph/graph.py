from core.chatbot.app.graph.state import State
 # from core.chatbot.app.graph.chain import router 
# from core.chatbot.app.graph.nodes import retrieve_answer_node, extract_information_travel, get_information_sale, selection_city
# from core.chatbot.app.graph.consts import TRACK_MY_ORDER, FAQ, BUY_CLOTHES
from core.chatbot.app.graph.persistence.redis.checkpointer import checkpointer
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import tools_condition
from core.chatbot.app.graph.assistant.assistant import Assistant, part_1_assistant_runnable, part_1_tools
from core.chatbot.app.graph.utilities import create_tool_node_with_fallback

workflow = StateGraph(State)

workflow.add_node("assistant", Assistant(part_1_assistant_runnable))
workflow.add_node("tools", create_tool_node_with_fallback(part_1_tools))

workflow.add_edge(START, "assistant")
workflow.add_conditional_edges(
    "assistant",
    tools_condition,
)
workflow.add_edge("tools", "assistant")



app = workflow.compile(checkpointer=checkpointer)
