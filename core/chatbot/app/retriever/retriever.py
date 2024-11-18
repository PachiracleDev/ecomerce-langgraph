from shared.db.milvus import get_answer_collection
from ingestion import get_text_embedding

def query(ask):
    if not ask:
        return None

    collection = get_answer_collection()
    query_embedding = get_text_embedding(ask)

    search_params = {
        "metric_type": "L2",
        "params": {
            "nprobe": 32
        }
    }

    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=3,
        expr=None,
        output_fields=["information"]
    ) 

    
    result_hits = []
    threshold = 0.4

    for hits in results:
        for hit in hits:
            if hit.distance <= threshold:
                result_hits.append(hit.entity.get("information"))
                
    return result_hits[0] if len(result_hits) > 0 else None