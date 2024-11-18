from core.chatbot.app.graph.persistence.redis.redis_saver import RedisSaver, initialize_async_pool, initialize_sync_pool
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from settings import settings

sync_redis_direct = initialize_sync_pool(host=settings.REDIS_HOST, port=int(settings.REDIS_PORT), db=0)
url_conn = f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}'
async_pool = initialize_async_pool(url=url_conn)

checkpointerredis = RedisSaver(sync_connection=sync_redis_direct, async_connection=async_pool)
checkpointer = MemorySaver()