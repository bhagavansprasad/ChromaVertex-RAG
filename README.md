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
  
## Content - Different operations on VectorDB (CromaDB)
### **Listing Files**
1. **Listing all files in a directory**  
   Script to list all files in a directory.
2. **Listing Git-tracked files**  
   Script to list files tracked by Git in the current repository.
3. **Listing Git-tracked PDF files**  
   Script to list PDF files tracked by Git.

### **PDF Operations**
4. **Basic PDF operations**  
   Script for performing basic PDF operations like merging, splitting, or extracting content.
5. **Chunk overlap demonstration**  
   Script to demonstrate chunk overlap concepts for splitting text or PDF content.
6. **Generating PDF embeddings**  
   Script to generate embeddings from PDF files.
7. **Creating page embeddings for PDFs**  
   Script to create embeddings for individual pages of a PDF.
8. **Creating chunk embeddings for PDFs**  
   Script to generate embeddings for specific chunks of text in a PDF.

### **Embedding File Formats**
9. **Saving PDF embeddings as CSV**  
   Script to save PDF embeddings into a CSV file.
10. **Saving PDF embeddings as JSON**  
   Script to save PDF embeddings into a JSON file.

### **Loading Embeddings**
11. **Loading embeddings from CSV**  
   Script to load embeddings from a CSV file.
12. **Loading embeddings from JSON**  
   Script to load embeddings from a JSON file.

### **ChromaDB Operations**
13. **Performing CRUD operations in ChromaDB**  
   Script to perform Create, Read, Update, and Delete operations in ChromaDB.
14. **Generating and adding embeddings to ChromaDB**  
   Script to generate embeddings and add them to ChromaDB.
15. **Storing embeddings persistently in ChromaDB**  
   Script to store embeddings persistently in ChromaDB.
16. **Executing multiple queries on ChromaDB**  
   Script to execute multiple queries on ChromaDB.
17. **Optimizing embedding generation**  
   Script to optimize embedding generation for better performance.

### **Embedding to Vector Database**
18. **Converting and storing text embeddings in vector database**  
   Script to convert text embeddings and store them in a vector database.
19. **Converting and storing PDF embeddings in vector database**  
   Script to convert PDF embeddings and store them in a vector database.
20. **Converting and storing CSV embeddings in vector database**  
   Script to convert embeddings from a CSV file and store them in a vector database.
21. **Converting and storing JSON embeddings in vector database**  
   Script to convert embeddings from a JSON file and store them in a vector database.

### **Searching in Vector Database**
22. **Searching vector database by ID**  
   Script to search the vector database by ID.
23. **Searching vector database by query**  
   Script to search the vector database using a query.
24. **Performing general search in vector database**  
   General script to perform searches in a vector database.
25. **Searching vector database by ID (alternative)**  
   Alternative script to search the vector database by ID.
26. **Executing advanced search queries in vector database**  
   Script to execute advanced search queries in the vector database.
27. **Create from CRUD operations on VectorDB**  
   Perform the "Create" operation in CRUD for the VectorDB.
28. **Read from CRUD operations on VectorDB**  
   Perform the "Read" operation in CRUD for the VectorDB.
29. **Update from CRUD operations on VectorDB**  
   Perform the "Update" operation in CRUD for the VectorDB.
30. **Delete from CRUD operations on VectorDB**  
   Perform the "Delete" operation in CRUD for the VectorDB.
31. **Create Query and Search to extract 'n' results**  
   Generate a query and search the database to retrieve 'n' results.
32. **Create Context with search results and pass to LLM**  
   Create context from the search results and pass it to the Large Language Model (LLM).
33. **Create embeddings from multiple PDF files**  
   Generate embeddings from several PDF files.
34. **Create embeddings for multiple PDF files and store them in different collections**  
   Generate embeddings for multiple PDF files and store them in separate collections.
35. **Create query and get the results from different collections**  
   Generate a query to fetch results from multiple collections.
36. **Create embeddings for multiple PDF files and store them in different vectorDBs**  
   Generate embeddings for multiple PDF files and store them in separate vectorDBs.
