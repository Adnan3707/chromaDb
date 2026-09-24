texts = [
    "Astronomy: A light-year measures distance, not time; it is the distance light travels in one year.",
    "History: The printing press helped books become more affordable and accelerated the spread of ideas in Europe.",
    "Biology: Plants convert light energy into chemical energy through photosynthesis, releasing oxygen as a byproduct.",
    "Technology: An algorithm is a step-by-step procedure used to solve a problem or complete a task.",
    "Geography: Ocean currents redistribute heat around Earth and influence regional climates.",
    "Economics: Inflation describes a sustained rise in the general price level, which reduces purchasing power over time.",
]

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

import chromadb
from chromadb.config import Settings
from pathlib import Path

chroma_client = chromadb.Client(
    Settings(
        persist_directory=str(Path(__file__).resolve().parent / 'chroma.db')
    )
)

collection = chroma_client.get_or_create_collection(
    name='Adnan-chroma-demo'
)

embeddings = []
ids = []

for i, text in enumerate(texts):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text,
    )
    embeddings.append(result.embeddings[0].values)
    ids.append(f"id_{i}")

collection.add(
    ids=ids,
    documents=texts,
    embeddings=embeddings
)

print("embeddings created sucessfully")

query='pogramming'
query_embedding = client.models.embed_content(
    model="gemini-embedding-2",
    contents=query,
).embeddings[0].values

result = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)
print(result['documents'])