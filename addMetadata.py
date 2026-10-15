import chromadb
client= chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("vehichles")

collection.update(
    documents=[
        "Bus carries passengers on road",
        "Plane flies across countries",
        "Boat travels on water",
        "Bicycle runs without fuel",        
    ],
    ids=['bus1','plane1','boat1','bike1'],
    metadatas=[
        {"type":"public_transport","fuel":"diesel"},
         {"type":"air_transport","fuel":"jet"},
          {"type":"water_transport","fuel":"diesel"},
           {"type":"personal_transport","fuel":"manual"},
    ]
    
)

print('data with meta data added sucessufully')