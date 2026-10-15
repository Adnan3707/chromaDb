import chromadb
# client = chromadb.Client()
client= chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(name='vehichles')

collection.add(
    documents=[
        "cars runs on land",
    ],
    ids=["car1"]
)