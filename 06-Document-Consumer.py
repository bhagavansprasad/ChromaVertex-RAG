# https://www.youtube.com/watch?v=QSW2L8dkaZk

import chromadb
import sys
from chromadb.utils import embedding_functions
import time
from pdbwhereami import whereami

def client_query_data(collection, query, result_count=2):
    # whereami(f"Query :{query}")    
    print(f"\nQuery :{query}")    
    details = ['distances', 'metadatas', 'documents']
    results = collection.query(query_texts = query, n_results=result_count, include=details)
    
    return(results)


def server_init_croma_db(vectdb_name, coll_name):
    # whereami()

    client = chromadb.PersistentClient(path=vectdb_name)
    
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
    collection = client.get_or_create_collection(name=coll_name, embedding_function=sentence_transformer_ef)
    return collection

def dump_collection_details(collection):
    while (True):
        count = collection.count()   
        whereami(f"collection count :{count}")
        time.sleep(1)

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
    {'query' : ['Kidnap'], 'qcount' : 2},
    {'query' : ['Swayamvara'], 'qcount' : 1},
]    

def main():
    vectdb_name = "aura-vectorDB"
    collection_name = "about-india"
   
    collection = server_init_croma_db(vectdb_name, collection_name)
    
    dump_collection_details(collection)
    
    for q in queries:
        reply = client_query_data(collection, q['query'], result_count=q['qcount'])
        dump_results(reply)
        
if (__name__ == "__main__"):
    main()
