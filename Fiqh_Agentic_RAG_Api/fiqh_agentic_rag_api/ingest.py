from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient
from llama_index.core.node_parser import SentenceSplitter

load_dotenv()

def ingest_data():
    print("🔄 Data ingestion process starting...")

    # Initialize Local Hugging Face Model
    print("📥 Loading local Hugging Face model (multilingual-e5-large")
    embed_model = HuggingFaceEmbedding(
        model_name="intfloat/multilingual-e5-large"
    )
    
    Settings.embed_model = embed_model
    Settings.llm = None
    
    # Chunking Settings
    Settings.text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=100)
    
    # Load Documents
    data_path = "./data"
    print(f"📂 Reading files from: {data_path}")
    documents = SimpleDirectoryReader(data_path, recursive=True).load_data()
    
    if not documents:
        print("ERROR: No files found in the specified directory!")
        return

    print(f"✅ Total {len(documents)} document chunks found.")

    # Connect to Qdrant
    client = QdrantClient(url="http://localhost:6333")
    
    # Because vector dimensions are different now.
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="fiqh_knowladge_base",
        embedding=HuggingFaceEmbedding(
            model_name="intfloat/multilingual-e5-large",
        )
    )
    
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    print("🚀 Embedding and Indexing started (Running locally)...")
    
    VectorStoreIndex.from_documents(
        documents=documents,
        storage_context=storage_context,
        show_progress=True
    )

    print("\n🎉 Success! All data ingested into Qdrant using local embeddings.")
    print("You can the chunks on http:localhost:6333/dashboard.")
    
if __name__ == "__main__":
    ingest_data()