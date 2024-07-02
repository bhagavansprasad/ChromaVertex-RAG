import chromadb 
from chromadb.db.base import UniqueConstraintError
import sys
import json

sys.path.append("/home/bhagavan/training/aura-llm/00-utils/")
from debug_helper import whereami

def Create_collection():
    cname = "example1"
    whereami()
    client = chromadb.Client()
    client.create_collection(name=cname)

def Create_existing_collection():
    cname = "example1"
    whereami()
    client = chromadb.Client()

    try:
        c1 = client.create_collection(name=cname)
        whereami(f'collection1 :{c1}')
    except UniqueConstraintError as err:
        whereami(f'Exception while creating collection :{err}')

def Get_non_existing_collection():
    cname = "example-none"
    whereami()
    client = chromadb.Client()

    try:
        c1 = client.get_collection(name=cname)
        whereami(f'collection1 :{c1}')
    except ValueError as err:
        whereami(f'Exception while creating collection :{err}')
        
def Get_existing_collection():
    cname = "example1"
    whereami()
    client = chromadb.Client()

    try:
        c1 = client.get_collection(name=cname)
        whereami(f'collection :{c1}')
    except chromadb.db.base.UniqueConstraintError as err:
        whereami(f'Exception while creating collection :{err}')
    else:
        whereami('Success in getting existing collection')

def Get_or_create_existing_collection():
    cname = "example1"
    whereami()
    client = chromadb.Client()

    try:
        c1 = client.get_or_create_collection(name=cname)
        whereami(f'collection1 :{c1}')
    except chromadb.db.base.UniqueConstraintError as err:
        whereami(f'Exception while creating collection :{err}')
        
def Get_or_create_new_collection():
    cname = "example-new"
    whereami()
    client = chromadb.Client()

    try:
        c1 = client.get_or_create_collection(name=cname)
        whereami(f'collection1 :{c1}')
    except chromadb.db.base.UniqueConstraintError as err:
        whereami(f'Exception while creating collection :{err}')

def Save_collection_to_disk():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)
    collection.upsert(
        documents=["C Programming Language", "Java Script", "Python Scripring and Programming Language"],
        metadatas=[{"type": "system"}, {"type": "script"}, {"type": "script"}],
        ids=["1", "2", "3"]
    )

def Load_collection_from_disk():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)
    
    print(collection.get())
    print()
    
def Query_collection():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    results = collection.query(
        query_texts=["script"],
        n_results=2,
        where={"type": "script"}
    )
    
    print(json.dumps(results, sort_keys=True, indent=4))
    print()

def Query_collection_Where():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    results = collection.query(
        query_texts=["script"],
        n_results=2,
        where={"type": "script"},
        where_document={"$contains": "Programming"}
    )
    
    print(json.dumps(results, sort_keys=True, indent=4))
    print()

def Query_collection_by_id():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    results = collection.get(ids=['2222'])
    
    print(json.dumps(results, sort_keys=True, indent=4))
    print()

def Update_documents():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    results = collection.get(ids=['2'])
    print("Before update...")
    print(json.dumps(results, sort_keys=True, indent=4))
    
    collection.update(
        documents=["Java Script"],
        metadatas=[{"type": "script"}],
        ids=["2"]
    )    

    results = collection.get(ids=['2'])
    print("\nAfter update...")
    print(json.dumps(results, sort_keys=True, indent=4))
    print()

def Upsert_documents():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    results = collection.get(ids=['4'])
    print("Before update...")
    print(json.dumps(results, sort_keys=True, indent=4))
    
    collection.upsert(
        documents=["Java Script"],
        metadatas=[{"type": "script"}],
        ids=["4"]
    )    

    results = collection.get(ids=['4'])
    print("\nAfter update...")
    print(json.dumps(results, sort_keys=True, indent=4))
    print()

def Delete_documents_by_id():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    count = collection.count()
    print(f"Before delete collection count :{count}")
   
    collection.delete(ids=["2"])    

    count = collection.count()
    print(f"After delete collection count :{count}")
    print()

def Get_documents_count():
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"
    client = chromadb.PersistentClient(path=vdb_name)
    collection = client.get_or_create_collection(name=cname)

    count = collection.count()
    print(f"Collection count :{count}")
    print()

def list_all_collections():
    client = chromadb.Client()
    client.get_or_create_collection(name="collection_one")
    client.get_or_create_collection(name="collection_two")

    print(client.list_collections())

    client.delete_collection(name="collection_one")
    client.delete_collection(name="collection_two")

    print(client.list_collections())
    print()

def main():
    whereami()
    # Create_collection()
    # Create_existing_collection()
    # Get_non_existing_collection()
    # Get_existing_collection()
    # Get_or_create_existing_collection()
    # Get_or_create_new_collection()
    # Save_collection_to_disk()
    # Load_collection_from_disk()
    # Query_collection()
    # Query_collection_Where()
    Query_collection_by_id()
    # Update_documents()
    # Upsert_documents()
    # Delete_documents_by_id()
    # Get_documents_count()
    # list_all_collections()
    
if (__name__ == "__main__"):
    main()
