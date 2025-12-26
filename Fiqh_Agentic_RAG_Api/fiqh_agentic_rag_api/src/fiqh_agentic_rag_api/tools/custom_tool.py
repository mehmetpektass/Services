import json
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient

class FiqhSearchInput(BaseModel):
    query: str = Field(..., description="The search keyword or question. Since the DB is Turkish, converting queries to Turkish yields better results.")

class FiqhSearchTool(BaseTool):
    name: str = "Fiqh_DB_Search_Tool"
    description: str = (
        "Use this tool to search for Islamic jurisprudence (Fiqh), verses, hadiths, "
        "and fatwas in the local vector database. The database content is mainly in Turkish."
    )
    args_schema: Type[BaseModel] = FiqhSearchInput

    def _run(self, query: str) -> str:
        try:
            embed_model = HuggingFaceEmbedding(
                model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
            )
            query_vector = embed_model.get_query_embedding(query)

            client = QdrantClient(url="http://localhost:6333")

            search_results = client.query_points(
                collection_name="fiqh_knowladge_base",
                query=query_vector,
                limit=5,
                with_payload=True,
            )

            all_results = []
            
            if search_results.points:
                for point in search_results.points:
                    if point.payload:

                        file_name = point.payload.get("file_name", "Unknown Source")
                        content = "No content found."
                        node_content_str = point.payload.get("_node_content")
                        
                        if node_content_str:
                            try:
                                node_data = json.loads(node_content_str)
                                content = node_data.get("text", "No content found inside node.")
                            except:
                                content = str(node_content_str)[:200] + "..."
                        else:
                            content = point.payload.get("text", "No content found.")

                        
                        score = point.score
                        all_results.append(f"Source: {file_name} (Confidence: {score:.2f}):\n{content}\n")
            else:
                return "Could not find any data related to this topic in the database!"
            
            return "\n".join(all_results)
        
        except Exception as e:
            return f"Database Error: {str(e)}"