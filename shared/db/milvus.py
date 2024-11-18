from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from settings import settings


def _connect():
    milvus_host = settings.MILVUS_HOST
    milvus_user = settings.MILVUS_USER
    milvus_password = settings.MILVUS_PASSWORD
    milvus_port = settings.MILVUS_PORT

    connections.connect("default", host=milvus_host, port=milvus_port, user=milvus_user, password=milvus_password)
    return connections

# Cerrar la conexión a Milvus
def disconnect():
    connections.disconnect("default")
     
def get_answer_collection():

    # Conectar a Milvus
    _connect()

    # Definir el esquema de la colección si no existe
    if not utility.has_collection("faq_collect_timeless"):
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1536),
            FieldSchema(name="information", dtype=DataType.VARCHAR, max_length=5000)
        ]
        
        schema = CollectionSchema(fields, description="Colección para almacenar los embeddings de preguntas frecuentes Timeless")
        
        # Crear la colección
        collection = Collection(name="faq_collect_timeless", schema=schema)
        
        # Crear un índice en los embeddings para acelerar la búsqueda
        index_params = {
            "index_type": "IVF_FLAT",  # Puedes ajustar el tipo de índice según tus necesidades
            "params": {"nlist": 128},
            "metric_type": "L2"
        }
        
        collection.create_index(field_name="embedding", index_params=index_params)
    else:
        collection = Collection("faq_collect_timeless")  # Obtener la colección si ya existe
    
    return collection