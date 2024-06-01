import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="test_collection")

collection.add("test_key", "test_value")