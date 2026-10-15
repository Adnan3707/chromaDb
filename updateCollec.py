import chromadb
client= chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("vehichles")

collection.update(
    ids=["bus1"],
    documents=[
        "The bus carries passengers across the city every day.This bus makes frequent stops along its route Passengers should wait safely at designated bus stops.",
        
    ]
)

print('Updated Record for bus')

record = collection.get(ids=["bus1"])
print(record)