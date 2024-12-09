import logging
from dump_utils import smart_print_with_list_trimming
from chromadb_utils import get_or_create_vector_db

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def read_collection_by_name(collection):
    results = collection.get()
    return results

def read_page_collection(collection, id_value):
    results = collection.get(ids=[id_value], include=["documents", "metadatas", "embeddings"])
    return results

def read_selected_sections_02(collection):
    results = collection.get(include=["documents"])
    return results

def dump_collection(collection):
    retval = read_collection_by_name(collection)
    smart_print_with_list_trimming(retval)

def dump_collection_by_id(collection, id):
    print(f"Search ChromaDB content id :{id}...")
    retval = read_page_collection(collection, id)
    smart_print_with_list_trimming(retval)

def main():
    vdb_name = "vectDB/pdf-vectorDB"
    coll_name = "cholas-embeddings"

    collection = get_or_create_vector_db(vdb_name, coll_name)

    print(f"Dumping Collection {coll_name}...")
    dump_collection(collection)
    
    dump_collection_by_id(collection, "page-id-1")

    dump_collection_by_id(collection, "chunk-id-1")

    print("Dumping ChromaDB ONLY document list...")
    retval = read_selected_sections_02(collection)
    smart_print_with_list_trimming(retval)
    # print(retval)
    print(retval['ids'])

    return
    
if __name__ == "__main__":
    main()
