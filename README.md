# Retrieval-Augmented Generation (RAG)

## What is RAG?
**Retrieval-Augmented Generation (RAG)** is a technique where a language model retrieves relevant documents from a knowledge base and then uses them as context to generate more accurate and reliable responses.

---

## Benefits of RAG
- **Up-to-date information**
- **Better privacy**
- **No limit on document size**

---

## Core Components of a RAG Application
To build a RAG-based application, we typically use the following components:

1. Document Loaders  
2. Text Splitters  
3. Vector Databases  
4. Retrievers  

---

## 1. Document Loaders

In LangChain, there are hundreds of **document loaders**.

Document loaders are components used to load data from various sources into a standardized format so that it can be used for:
- Chunking
- Embedding
- Retrieval
- Generation

### Standardized Document Format

All loaders return data in the **Document** format:

```python
Document(
    page_content="the actual text content",
    metadata={"source": "filename.pdf", ...}
)
```

Each loader returns a **list of Document objects**.

---

## TextLoader

**TextLoader** is a simple and commonly used document loader in LangChain that reads plain text (`.txt`) files and converts them into `Document` objects.

### Use Cases
- Chat logs  
- Transcripts  
- Code snippets  
- Any plain text data  

### Limitation
- Works **only** with `.txt` files.

---

## PyPDFLoader

**PyPDFLoader** is a document loader used to load content from PDF files and convert each page into a separate `Document` object.

### Example Output
If a PDF contains 20 pages, PyPDFLoader will return:

```python
[
    Document(page_content="Text from page 1", metadata={"page": 0, "source": "file.pdf"}),
    Document(page_content="Text from page 2", metadata={"page": 1, "source": "file.pdf"}),
    ...
]
```

This means:
- One `Document` object per page
- Each document contains page content and metadata

### Limitations
- Internally uses the **PyPDF** library
- Not suitable for:
  - Scanned PDFs
  - Image-based PDFs
  - Complex layouts

### When to Use
- PDFs that are mostly **text-based**

---

## Other PDF Loaders in LangChain

To handle different PDF formats, LangChain provides additional loaders:

| Use Case | Recommended Loader |
|--------|-------------------|
| PDFs with tables/columns | `PDFPlumberLoader` |
| Scanned or image PDFs | `UnstructuredPDFLoader`, `AmazonTextractPDFLoader` |
| Layout-aware PDFs with images | `PyMuPDFLoader` |

---

## DirectoryLoader

If you have **multiple files** (text, PDFs, CSVs) inside a folder, you can load them all at once using **DirectoryLoader**.

### What It Does
- Loads multiple documents from a directory
- Supports different file types
- Works with recursive folder structures

### Glob Patterns

| Pattern | Description |
|-------|------------|
| `"**/*.txt"` | All `.txt` files in all subfolders |
| `"*.pdf"` | All `.pdf` files in the root directory |
| `"data/*.csv"` | All `.csv` files in the `data/` folder |
| `"**/*"` | All files of any type in all folders |

`**` enables recursive search through subfolders.

---

## Eager Loading vs Lazy Loading

### `load()` – Eager Loading
- Loads **all documents at once**
- Returns a list of `Document` objects
- Uses more memory
- Best for:
  - Small number of documents
  - When everything needs to be available immediately

### `lazy_load()` – Lazy Loading
- Loads documents **on demand**
- Returns a **generator** of `Document` objects
- More memory-efficient
- Best for:
  - Large documents
  - Large number of files

---

## Web-Based Document Loaders

Web-based loaders are used to extract content from web pages (URLs).

### Libraries Used
- `requests`
- `BeautifulSoup`

### When to Use
- Blogs
- News articles
- Documentation pages
- Static, text-based public web pages

### Limitations
- Does **not** handle JavaScript-heavy pages  
  - Use `SeleniumURLLoader` for dynamic content
- Loads only static HTML content

---

## CSV Loader

- Loads CSV files row by row
- Each row is converted into a **separate Document object**
- Useful for structured tabular data

---

## Summary

Document loaders are the first and most critical step in building a RAG pipeline. Choosing the right loader based on your data type ensures better chunking, embeddings, and retrieval quality.

---

**Happy Building with LangChain & RAG 🚀**
