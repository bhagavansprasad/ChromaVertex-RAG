import chromadb

def list_all_collections(vdb_name):
    client = chromadb.PersistentClient(path=vdb_name)
    return client.list_collections()

def dump_collection_entries(collection):
    data = collection.get()
    print(f"Collection Details:\n{data}")
    print()

def dump_selected_entries(collection):
    entries = ["documents", "metadatas"]
    data = collection.get(include=entries)
    print(f"Dump selected entries :{entries}")
    print(data)
    print()

def vdb_list_collections(collections):
    for collection in collections:
        print(f"Collection ID: {collection.id}")

def main():
    vdb_name = "vectDB/pdf-vectorDB"
    
    print(f"VectorDB :{vdb_name}")    
    collections = list_all_collections(vdb_name)
    print()

    for coll in collections:
        dump_collection_entries(coll)

    for coll in collections:
        dump_selected_entries(coll)

    vdb_list_collections(collections)
    
    return
    
if __name__ == "__main__":
    main()
