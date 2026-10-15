import chromadb
client = chromadb.Client()

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

# query the collection

results = collection.query(
    query_texts=['vechicle that run on road']
    ,
    n_results=2
)
print(results)