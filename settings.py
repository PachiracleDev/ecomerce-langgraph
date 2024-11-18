import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "ChatBot Timeless"
    API_URL: str = os.getenv("API_URL")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    PORT: int = os.getenv("PORT", 5000)
    DATABASE_URI: str = os.getenv("DATABASE_URI")
    REDIS_HOST: str = os.getenv("REDIS_HOST")
    REDIS_PORT: int = os.getenv("REDIS_PORT")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    ##AWS
    AWS_BUCKET_NAME: str = os.getenv("AWS_BUCKET_NAME")
    AWS_REGION_NAME: str = os.getenv("AWS_REGION_NAME")
    AWS_ACCESS_KEY: str = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str = os.getenv("AWS_SECRET_KEY")
    AWS_CLOUDFRONT: str = os.getenv("AWS_CLOUDFRONT")
    
    #MONGO
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")
    
    #MILVUS
    MILVUS_HOST: str = os.getenv("MILVUS_HOST")
    MILVUS_USER: str = os.getenv("MILVUS_USER")
    MILVUS_PASSWORD: str = os.getenv("MILVUS_PASSWORD")
    MILVUS_PORT: int = os.getenv("MILVUS_PORT")

settings = Settings()
