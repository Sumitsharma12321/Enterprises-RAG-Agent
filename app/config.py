import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # ------ Gemini Embeddings -------
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # ------ Vector DB(QDRANT) ----
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION = "enterprise_rag"
    
    # -----Reasoning Engine(GROQ)-----
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")

    # LLM Gateway
    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    PORTKEY_CONFIG = os.getenv("PORTKEY_CONFIG")
    GROQ_SLUG = "enterprise-rag"   # primary: "@enterprise-rag/llama-3.3-70b-versatile"
    GROQ_SLUG_2 = "enterprise-rag2"  # fallback:"@enterprise-rag2/llama-3.1-8b-instant"

settings = Settings()
  
