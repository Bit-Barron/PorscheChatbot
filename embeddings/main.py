import json
import chromadb
from sentence_transformers import SentenceTransformer
import numpy as np

# Step 2: Define a settings class
class Settings:
    def __init__(self, **entries):
        self.__dict__.update(entries)

# Load configuration
with open('chromadb_config.json', 'r') as f:
    config_dict = json.load(f)

# Create a settings object
config = Settings(**config_dict)

# Initialize ChromaDB client with configuration settings
client = chromadb.Client(settings=config)
collection = client.create_collection("text_embeddings")

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

texts = [
    "This is a sentence.",
    "This is another sentence.",
    "ChromaDB is great for storing embeddings.",
    "How do you store embeddings efficiently?",
    "Machine learning models generate embeddings."
]

# Generate embeddings for the text data
embeddings = model.encode(texts)

# Convert embeddings to list format for ChromaDB
embeddings_list = embeddings.tolist()
ids = [f"text_{i}" for i in range(len(texts))]

# Add embeddings to the collection
collection.add(
    ids=ids,
    vectors=embeddings_list
)

# Example query to find similar texts
query_text = "How can we store text embeddings?"
query_embedding = model.encode([query_text]).tolist()

results = collection.query(query_embedding, top_k=3)

print("Query results:")
for result in results:
    print(result)

# Retrieve the actual text for the results
result_ids = [result['id'] for result in results]
retrieved_texts = [texts[int(id.split('_')[1])] for id in result_ids]

print("\nSimilar texts to query:")
for text in retrieved_texts:
    print(text)
