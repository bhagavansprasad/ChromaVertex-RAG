from chromadb_utils import get_or_create_vector_db
from chromadb_utils import vdb_search_by_query
from chromadb_utils import vdb_search_by_query_ids
from vertexai.generative_models import GenerativeModel
from vertexai.generative_models import GenerationConfig
    
def dump_search_results(query_results):
    ids = query_results['ids'][0]
    docs = query_results['documents'][0]
    distances = query_results['distances'][0]
    
    for i, (id, doc, distance) in enumerate(zip(ids, docs, distances), 1):
        print(f"{i}. ID: {id}")
        print(f"doc :{doc}")
        print(f"distance :{distance}")
        print()
    return 0

def get_documents_by_query(vdb_name, coll_name, query_text):

    collection = get_or_create_vector_db(vdb_name, coll_name)

    results = vdb_search_by_query_ids(collection=collection, query_text=query_text, only_chunks=True)
    dump_search_results(results)

    documents = [doc for doc in results["documents"][0]]
    
    return documents

def prompt_llm(prompt, query):
    gen_config = GenerationConfig(temperature=1.0) # influences the creativity and randomness of the generated text.
    gen_config = GenerationConfig(temperature=1.0, response_mime_type='application/json')
    model = GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt, generation_config=gen_config)
    
    print("-" * 75)
    print(f"Query :{query}")
    # print(f"Prompt :{prompt}")
    print(f"Response :\n{response.text}")
    print("-" * 75)

def build_context_search_llm(query, vdb_name, collection):
    documents = get_documents_by_query(vdb_name, collection, query)

    context = "\n\n".join(documents)
    MAX_TOKENS = 4096  # Example token limit, adjust based on your model
    context = context[:MAX_TOKENS]

    # "Focus on the following context: [Provide the relevant information here]."
    # Construct the input for the LLM
    prompt = f"""
    "{query}. Focus on the following context: [{context}]."
   
    ### Rules:
    1. Do not add any information not present in the context.
    2. If the answer is not found in the context, reply with "The information is not available in the provided context."

    Answer:
    """

    return prompt
    
def main():
    prompts = [
        {
            "query_text": "They divided their empire into, what?",
            "vdb_name": "vectDB/pdf-vectorDB",
            "collection": "cholas-embeddings"
        },
        {
            "query_text": "Who is Rama?",
            "vdb_name": "vectDB/pdf-vectorDB",
            "collection": "ramayan-embeddings"
        },
        {
            "query_text": "During which time period did the Mahabharata take place?",
            "vdb_name": "vectDB/pdf-vectorDB",
            "collection": "mahabharata-embeddings"
        },
    ]

    for q in prompts:
        query = q['query_text']
        vdb_name = q['vdb_name']
        collection = q['collection']
        context = build_context_search_llm(query, vdb_name, collection)
        
        prompt_llm(context, query)
   
    return True
  
if __name__ == "__main__":
    main()
