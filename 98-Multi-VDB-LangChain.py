# from langchain_community.vectorstores import Chroma
# from langchain_google_vertexai import VertexAIEmbeddings, VertexAI
# # from vertexai.generative_models import GenerativeModel

# # Define and rebuild VertexAIEmbeddings
# VertexAIEmbeddings._LanguageModel = None
# VertexAIEmbeddings.model_rebuild()

# # Initialize LLM
# VertexAI._LanguageModel = None
# VertexAI.model_rebuild()
# llm = VertexAI(model="gemini-1.5-flash", temperature=1.0)

# # Initialize embeddings
# embeddings = VertexAIEmbeddings(project_id="xxxxxx")

# # VectorDB connections
# vector_dbs = {
#     "cholas-vdb": Chroma(embedding_function=embeddings, persist_directory="vectDB/cholas-vdb"),
#     "ramayan-vdb": Chroma(embedding_function=embeddings, persist_directory="vectDB/ramayan-vdb"),
#     "mahabharata-vdb": Chroma(embedding_function=embeddings, persist_directory="vectDB/mahabharata-vdb")
# }

# def build_context(vdb_name, query_text, top_k=5):
#     vector_db = vector_dbs[vdb_name]
#     results = vector_db.similarity_search(query_text, k=top_k)
#     documents = [result.page_content for result in results]
#     return "\n\n".join(documents)

# def generate_response(vdb_name, query_text):
#     context = build_context(vdb_name, query_text)
#     prompt_template = """
#     "{query}. Focus on the following context: [{context}].
    
#     ### Rules:
#     1. Do not add any information not present in the context.
#     2. If the answer is not found in the context, reply with 'The information is not available in the provided context.'
    
#     Answer:
#     """
#     prompt = prompt_template.format(query=query_text, context=context[:4096])
#     response = llm.generate(prompt)
#     print(f"Query: {query_text}")
#     print(f"Response:\n{response}\n{'-' * 75}")

# def main():
#     prompts = [
#         {"query_text": "They divided their empire into, what?", "vdb_name": "cholas-vdb"},
#         {"query_text": "Who is Rama?", "vdb_name": "ramayan-vdb"},
#         {"query_text": "During which time period did the Mahabharata take place?", "vdb_name": "mahabharata-vdb"}
#     ]
#     for prompt in prompts:
#         generate_response(prompt["vdb_name"], prompt["query_text"])

if __name__ == "__main__":
    print("No implimentation YET, exiting...")
    exit(1)
    main()
