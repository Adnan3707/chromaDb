import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehichles")
print(collection.get())