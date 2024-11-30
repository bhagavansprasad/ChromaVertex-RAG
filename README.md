# RAG Basics
## Setup
```sh
pip install .
```
## Content - Different operations on VectorDB (CromaDB)
1. List all files in a folder
2. List all files from a git repo cloned folder
3. List only pdf files from cloned folder
4. Create CRUD operations on PDF files using Fitz
5. Create Chunks from PDF content
6. Create embenddings for PDF content
7. Create embenddings for each Page and for whole file
8. Create embenddings for Chunked-text, Page and for whole file
9. Create embenddings and store Pandas Dataframe and to csv file
10. Create embenddings and store Pandas Dataframe and to json file
11. Load embenddings from csv to Pandas Dataframe
12. Load embenddings from json to Pandas Dataframe
13. ChromaDB CRUD operations
13. Basic String embeddings to VectorDB
14. Search VectorDB by ID
15. Search VectorDB by Query
16. Create PDF file's embeddings and store in VectorDB *
17. Load embeddings from csv and store in VectorDB * - NOT WORKING
18. Load embeddings from json and store in VectorDB * - NOT WORKING
19. Search in VectorDB (ChromaDB)
20. Search VectorDB
21. Create Query and search in VectorDB (ChromaDB)
19. Create Query and Search extract 'n' results *
20. Create Context with search results and pass to LLM *
22. Create Query and Search extract 'n' results from VectorDB and pass to LLM *
23. Create embenddings from multiple PDF files *
24. Create embenddings multiple PDF files and store in different VectorDBs  *
25. Create query and get the results from different VectorDBs *
26. Dump VectorDB details *
27. Do 'Create' from CRUD operations on VectorDB *
28. Do 'Read' from CRUD operations on VectorDB *
29. Do 'Update' from CRUD operations on VectorDB *
30. Do 'Delete' from CRUD operations on VectorDB *


### Points to Note while creating embeddings

- A query is valid only when the dimensions of the search query embedding match those of the stored chunk embedding.
- To ensure high-quality results when generating embeddings from a PDF file, follow these recommendations:
  - **Create only chunked embeddings.** Avoid generating per-page or entire file embeddings to prevent duplication.
  - Generating both chunked, page-level, and file-level embeddings can lead to duplicate results.
- Include the following details in the metadata while creating embeddings:
  - File name
  - Page number
  - Chunk number
  - Chunk size