from fastapi import APIRouter
from core.chatbot.app.graph.graph import app

router = APIRouter(prefix="/web")

@router.post("/send")
async def send_message(
    body: dict
):
    config = {
        "configurable": {
            "thread_id": body['thread_id'],
        }
    }

    input = {
        "messages": ("user", body['message']),
        "user_info": {
            "name": "Patrick",
            "user_id": 2
        }
    }

    result = await app.ainvoke( input, config=config)

    return  result["messages"]