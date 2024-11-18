# from typing import Literal

# from langchain_core.prompts import ChatPromptTemplate
# from pydantic import BaseModel, Field
# from langchain_openai import ChatOpenAI
# from core.chatbot.app.graph.state import GraphState
# from core.chatbot.app.graph.consts import FAQ, BUY_CLOTHES, TRACK_MY_ORDER


# class RouteQuery(BaseModel):
#     """Obtenemos el topic del mensaje"""
#     topic: Literal["faq", "buy_clothes", 'track_my_order'] = Field(
#         ...,
#         description="Dado el mensaje del usuario, elija dirigirla a faq, buy_clothes o track_my_order",
#     )


# llm = ChatOpenAI(temperature=0)
# structured_llm_router = llm.with_structured_output(RouteQuery)

# system = """Clasifica la intención del usuario.
# Usa 'faq' para obtener la respuesta de una pregunta frecuente.
# Usa 'buy_clothes' cuando el usuario quiere saber y/o comprar ropa.
# Usa 'track_my_order' para obtener la información, estado o rastreo de su venta.
# """

# route_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system),
#         ("human", "{question}"),
#     ]
# )

# question_router = route_prompt | structured_llm_router

# def route_question(state: GraphState) -> str:
    
#     topic: RouteQuery = question_router.invoke({"question": state["message_user"]})
    
    
#     match topic.topic:
#         case "faq":
#             return FAQ
#         case "track_my_order":
#             return TRACK_MY_ORDER
#         case "buy_clothes":
#             print("---GET_TICKET_INFORMATION---")
#             return BUY_CLOTHES
#         case _:
#             raise ValueError(f"Unknown topic: {topic.topic}")