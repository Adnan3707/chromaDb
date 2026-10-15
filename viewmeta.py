import chromadb
# client = chromadb.Client()
client= chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name='vehichles')

data = collection.get(include=["documents","metadatas"])

for i,doc,meta in zip(data["ids"],data["documents"],data["metadatas"]):
    print(f'{i} -->  {doc} --> {meta}')