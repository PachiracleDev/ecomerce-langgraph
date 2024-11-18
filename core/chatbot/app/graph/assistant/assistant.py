from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from datetime import datetime
from core.chatbot.app.graph.state import State
from core.chatbot.app.graph.tools import lookup_ask, get_categories, get_products, add_to_cart, get_cart, remove_from_cart, get_cart_total, update_item_cart, clear_cart

class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    async def __call__(self, state: State, config: RunnableConfig):
        while True:
     
            result = await self.runnable.ainvoke(state)
            # If the LLM happens to return an empty response, we will re-prompt it
            # for an actual response.
            if not result.tool_calls and (
                not result.content
                or isinstance(result.content, list)
                and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Responder con una salida real.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}


llm = ChatOpenAI(temperature=1)

primary_assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Eres un asistente de la empresa de ropa Timeless, que ayuda a los clientes a encontrar y comprar ropa."
            "Usa las herramientas a continuación para ayudar a los clientes a encontrar, comprar ropa y buscar preguntas frecuentes."
            " Al realizar una búsqueda, sea persistente. Amplíe los límites de su consulta si la primera búsqueda no arroja resultados. "
            " Si una búsqueda no da resultados, amplíe su búsqueda antes de darse por vencido."
            "\n\Informacion del usuario: \n<User>\n{user_info}\n</User>"
            "\nTiempo actual: {time}.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

part_1_tools = [
    lookup_ask,
    get_categories,
    get_products,
    add_to_cart,
    get_cart,
    remove_from_cart,
    get_cart_total,
    update_item_cart,
    clear_cart,
]
part_1_assistant_runnable = primary_assistant_prompt | llm.bind_tools(part_1_tools)

