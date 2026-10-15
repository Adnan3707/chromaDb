import chromadb
client= chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(name='vehichles')

collection.add(
    documents=[
        "cars runs on land",
        "planes flies in the sky",
        "boat travels on water",
        "bus is public transport on road"
    ],
    ids=["car1","plane1","boat1","bus1"]
)

# collection = client.get_collection("vehichles")
data = collection.get()

for i,doc in zip(data["ids"],data["documents"]):
    print(f'{i} -->  {doc}')