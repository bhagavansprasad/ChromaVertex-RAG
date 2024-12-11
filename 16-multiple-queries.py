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
    
    return(results)

def producer_stream_csv_data(collection, csvdata, batchsize=0, queue=None):
    documents = []
    metadata = []
    ids = []
    rfd = 0
    whereami(f"Embedding csv data csv file name:{csvdata}")

    try:
        rfd = open(csvdata)
    except IOError as err:
        whereami(f"Error in opening file err :{err}")
        exit(1)

    csvfd = csv.reader(rfd)
    next(csvfd) # skip column header
        
    for i, row in enumerate(csvfd, 2):
        documents.append(row[2])
        metadata.append({'type' : row[1]})
        ids.append(row[0])

        results = collection.get(ids=row[0])
        if (len(results['ids']) != 0):
            continue
        
        whereami(f"ids      :{ids}")
        whereami(f"metadata :{metadata}")
        whereami(f"docs     :{documents}")
        print()
        collection.add(documents=documents, metadatas=metadata, ids=ids)
        metadata = []
        documents = []
        ids = []
        
    whereami(f"Finished Embedding csv data :{csvdata}")

def server_init_croma_db(vectdb_name, coll_name):
    whereami()

    client = chromadb.PersistentClient(path=vectdb_name)
    
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
    collection = client.get_or_create_collection(name=coll_name, embedding_function=sentence_transformer_ef)
    return collection

def producer_create_embeddings(collection, csvdata):

    producer_stream_csv_data(collection, csvdata)
    return

def dump_collection_details(collection):
    print(collection.get())
    count = collection.count()   
    print()
    whereami(f"collection count :{count}")
    print()

def delete_collection_by_name(collection_name):
    client = chromadb.Client()
    
    try:
        client.delete_collection(name=collection_name)
        whereami(f"Successfully Deleted collection :{collection_name}")
    except ValueError as err:
        whereami(f"Collection doesn't exists :{err}")
        pass
        
    return

def dump_results(jdata):
    # jdata = json.loads(reply)

    ids = jdata["ids"][0]
    metadata = jdata["metadatas"][0]
    documents = jdata["documents"][0]

    # whereami(f"ids       :{ids}")
    # whereami(f"metadata  :{metadata}")
    # whereami(f"documents :{documents}")

    for i, id in enumerate(ids):
        print(f"\t{id}: {metadata[i]['type']} -->{documents[i]}")

queries = [
    {'query' : ['Kidnap'], 'similarity_search_count' : 5},
    {'query' : ['Swayamvara'], 'similarity_search_count' : 2},
]    

def main():
    vectdb_name = "aura-vectorDB"
    collection_name = "about-india"
    csvdata = "../data/indian_history.csv"
    
    # delete_collection_by_name(collection_name)
    
    collection = server_init_croma_db(vectdb_name, collection_name)
    producer_create_embeddings(collection, csvdata)

    # dump_collection_details(collection)

    for q in queries:
        reply = client_query_data(collection, q['query'], result_count=q['similarity_search_count'])
        dump_results(reply)
        
if (__name__ == "__main__"):
    main()
