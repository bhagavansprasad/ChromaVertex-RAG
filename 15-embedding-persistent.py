# https://www.youtube.com/watch?v=QSW2L8dkaZk

import json
import chromadb
import csv
import sys
from chromadb.utils import embedding_functions
from pdbwhereami import whereami

def client_query_data(collection, query, result_count=2):
    whereami(f"Querying: Query :{query}")    

    details = ['distances', 'metadatas', 'documents']
    results = collection.query(query_texts = query, n_results=result_count, include=details)

    whereami(f"Go the results....")    
    data = json.dumps(results, indent=4)

    return(data)

def producer_stream_csv_data(fname, collection, batchsize=0, queue=None):
    documents = []
    metadata = []
    ids = []
    rfd = 0
    whereami(f"Embedding csv data csv file name:{fname}")

    try:
        rfd = open(fname)
    except IOError as err:
        whereami(f"Error in opening file err :{err}")
        exit(1)

    csvfd = csv.reader(rfd)
    next(csvfd) # skip column header
        
    for i, row in enumerate(csvfd, 2):
        documents.append(row[2])
        metadata.append({'type' : row[1]})
        ids.append(row[0])
        
        whereami(f"ids      :{ids}")
        whereami(f"metadata :{metadata}")
        whereami(f"docs     :{documents}")
        print()
        collection.add(documents=documents, metadatas=metadata, ids=ids)
        metadata = []
        documents = []
        ids = []
        
    whereami(f"Finished Embedding csv data :{fname}")

def server_init_croma_db(coll_name):
    whereami()
    vdb_name = "aura-vectorDB"
    cname = "programming-coll"

    # chroma_client = chromadb.Client()
    client = chromadb.PersistentClient(path=vdb_name)
    
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
    collection = client.get_or_create_collection(name=coll_name, embedding_function=sentence_transformer_ef)
    return collection

def producer_create_embeddings(collection):
    whereami()
    fname = "../data/indian_history.csv"

    producer_stream_csv_data(fname, collection)    
    return

def dump_collection_details(collection):
    print(collection.get())
    count = collection.count()   
    print()
    whereami(f"collection count :{count}")
    print()

def main():
    coll_name = "menu_collection"
    
    whereami()
    collection = server_init_croma_db(coll_name)
    
    producer_create_embeddings(collection)

    dump_collection_details(collection)

    query = ["Who is Hanuman?"]
    reply = client_query_data(collection, query, result_count=5)
    whereami(reply)
    
if (__name__ == "__main__"):
    main()
