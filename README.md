# RAG Basics  - A Beginner's Practical Guide to Vector Database: ChromaDB

## Introduction to ChromaDB
ChromaDB is a high-performance, scalable vector database designed to store, manage, and retrieve high-dimensional vectors efficiently. It is especially useful in applications involving machine learning, data science, and any field that requires fast and accurate similarity searches.

## Key Features
* High Performance: Optimized for speed and efficiency in handling large-scale vector data.
* Scalability: Easily scales to handle growing datasets and increasing query loads.
* Versatility: Supports various types of vector data and query methods.
* Integration: Compatible with popular machine learning frameworks and data processing libraries.

## Installing chromadb & dependencies
```sh
sudo apt-get install libprotobuf-dev
pip install .
```

## Basic Concepts
### Vectors
Vectors are arrays of numbers representing data points in a high-dimensional space. ChromaDB specializes in managing these vectors and performing operations such as similarity searches.

### Collections
Collections are groups of vectors stored together in ChromaDB. They help organize and manage the data efficiently.

### Indexes
Indexes in ChromaDB are data structures that allow for fast retrieval of vectors based on similarity measures.

### **Listing Files**
1. **`01-list-files.py`**  
   Script to list all files in a directory.
2. **`02-list-git-files.py`**  
   Script to list files tracked by Git in the current repository.
3. **`03-git-pdfs.py`**  
   Script to list PDF files tracked by Git.

### **PDF Operations**
4. **`04-pdf-ops`**  
   Script for performing basic PDF operations like merging, splitting, or extracting content.
5. **`05-chunk-overlap-basics.py`**  
   Script to demonstrate chunk overlap concepts for splitting text or PDF content.
6. **`06-pdf-embeddings.py`**  
   Script to generate embeddings from PDF files.
7. **`07-page-embeddings.py`**  
   Script to create embeddings for individual pages of a PDF.
8. **`08-chunk-embeddings.py`**  
   Script to generate embeddings for specific chunks of text in a PDF.

### **Embedding File Formats**
9. **`09-pdf-embeddings-csv.py`**  
   Script to save PDF embeddings into a CSV file.
10. **`10-pdf-embeddings-json.py`**  
   Script to save PDF embeddings into a JSON file.

### **Loading Embeddings**
11. **`11-Load-Emb-From-csv.py`**  
   Script to load embeddings from a CSV file.
12. **`12-Load-Emb-From-json.py`**  
   Script to load embeddings from a JSON file.

### **ChromaDB Operations**
13. **`13-CRUD-CromaDB.py`**  
   Script to perform Create, Read, Update, and Delete operations in ChromaDB.
14. **`14-Embedding-Producer.py`**  
   Script to generate embeddings and add them to ChromaDB.
15. **`15-embedding-persistent.py`**  
   Script to store embeddings persistently in ChromaDB.
16. **`16-multiple-queries.py`**  
   Script to execute multiple queries on ChromaDB.
17. **`17-optimized-embedding.py`**  
   Script to optimize embedding generation for better performance.

### **Embedding to Vector Database**
18. **`18-text-Emb-to-Vectordb.py`**  
   Script to convert text embeddings and store them in a vector database.
19. **`21-Pdf-Emb-to-Vectordb.py`**  
   Script to convert PDF embeddings and store them in a vector database.
20. **`22-CSV-Emb-to-Vectordb.py`**  
   Script to convert embeddings from a CSV file and store them in a vector database.
21. **`23-JSON-Emb-to-Vectordb.py`**  
   Script to convert embeddings from a JSON file and store them in a vector database.

### **Searching in Vector Database**
22. **`19-Search-VDB-by-ID.py`**  
   Script to search the vector database by ID.
23. **`20-Search-VDB-by-Query.py`**  
   Script to search the vector database using a query.
24. **`24-Search-VDB.py`**  
   General script to perform searches in a vector database.
25. **`25-Search-VDB-by-ID.py`**  
   Alternative script to search the vector database by ID.
26. **`26-vdb-search-query.py`**  
   Script to execute advanced search queries in the vector database.

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