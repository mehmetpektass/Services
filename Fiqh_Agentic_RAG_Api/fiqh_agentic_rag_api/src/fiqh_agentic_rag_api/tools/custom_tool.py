import json
from crewai.tools import BaseTool
from typing import Type, Optional, Any
from pydantic import BaseModel, Field, PrivateAttr
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient

# --- GLOBAL MEMORY (Singleton Pattern) ---
_GLOBAL_EMBED_MODEL = None

class FiqhSearchInput(BaseModel):
    query: str = Field(..., description="The search keyword or question.")

class FiqhSearchTool(BaseTool):
    name: str = "Fiqh_DB_Search_Tool"
    description: str = "Search for Islamic jurisprudence (Fiqh) texts."
    args_schema: Type[BaseModel] = FiqhSearchInput
    
    # Private attribute to hold the model instance within the class
    _embed_model: Optional[Any] = PrivateAttr(default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global _GLOBAL_EMBED_MODEL
        
        # Load model ONLY if it's not already in global memory
        if _GLOBAL_EMBED_MODEL is None:
            print("⚙️ Loading Embedding Model (This should appear ONLY ONCE)...")
            _GLOBAL_EMBED_MODEL = HuggingFaceEmbedding(
                model_name="intfloat/multilingual-e5-large"
            )
            print("✅ Model Loaded into Memory!")
        else:
            print("⚡ Model Ready (Using Cached Version)...")
            
        # Assign the global model to this instance
        self._embed_model = _GLOBAL_EMBED_MODEL

    def _run(self, query: str) -> str:
        try:
            # Generate embedding using the cached model
            query_with_prefix = f"query: {query}"
            query_vector = self._embed_model.get_query_embedding(query_with_prefix)
            
            client = QdrantClient(url="http://localhost:6333")
            
            search_results = client.query_points(
                collection_name="fiqh_knowladge_base",
                query=query_vector,
                limit=5,
                score_threshold=0.5,
                with_payload=True,
            )

            all_results = []
            
            high_quality_points = [p for p in search_results.points if p.score >= 0.5][:3]
            
            if high_quality_points:
                for point in high_quality_points:
                    if point.payload:
                        file_name = point.payload.get("file_name", "Unknown")
                        content = "No content."
                        node_content_str = point.payload.get("_node_content")
                        
                        # Safe JSON parsing for content
                        if node_content_str:
                            try:
                                node_data = json.loads(node_content_str)
                                content = node_data.get("text", "")
                            except:
                                content = point.payload.get("text", "")
                        else:
                            content = point.payload.get("text", "")
                        
                        # Truncate content to save tokens (Max 1500 chars)
                        if len(content) > 500:
                            content = content[:500] + "... (truncated)"

                        score = point.score
                        all_results.append(f"Source: {file_name} (Conf: {score:.2f}):\n{content}\n")
            else:
                return "No relevant data found. Please try rephrasing your question.(İlgili veri bulunamadı. Lütfen sorunuzu yeniden ifade etmeyi deneyin.)"
            
            return "\n".join(all_results)
        
        except Exception as e:
            return f"Error: {str(e)}"