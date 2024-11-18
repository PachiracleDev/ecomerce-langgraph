from openai import OpenAI
from typing import List
from shared.db.milvus import get_answer_collection


def get_text_embedding(answer: str) -> List[float]:
    client = OpenAI()
    
    response = client.embeddings.create(
        input=answer,
        model="text-embedding-ada-002"
    )
    
    return response.data[0].embedding




def save_faq_to_collection(hits: list[str]):
    try:
        embeddings = [get_text_embedding(texts) for texts in hits]

        if len(hits) != len(embeddings):
            print("Error: No se pudo obtener los embeddings de las respuestas.")
            return

        
        entities = {
            "embedding": [],
            "information": []
        }

        for idx, hit_information in enumerate(hits):
            entities["embedding"].append(embeddings[idx])
            entities['information'].append(hit_information)

        # Conectar a Milvus
        milvus_collection = get_answer_collection()

        # Insertar los datos en Milvus
        milvus_result = milvus_collection.insert([
            entities["embedding"],
            entities["information"],
        ])

        # Convertir el resultado de Milvus a una lista para que sea serializable
        milvus_primary_keys = list(milvus_result.primary_keys)
        
        return milvus_primary_keys
    
    except Exception as e:
        print(f"Error al guardar las preguntas frecuentes: {e}")
        raise e



def execute():
    
    hits = []
    
    with open("faq.txt", "r", encoding="utf-8") as file:
        for line in file:
            hits.append(line)
    
    primary_keys = save_faq_to_collection(hits)
    
    print(primary_keys, "primary_keys")
        
if __name__ == "__main__":
    execute()
    