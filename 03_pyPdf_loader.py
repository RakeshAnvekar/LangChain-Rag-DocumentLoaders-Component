from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('dummy_two_page_document.pdf')
docs = loader.load()
print(f'Number of documents loaded: {len(docs)}')
print(f'Content of the first document:\n{docs[0].page_content}')
print(f'Metadata of the first document:\n{docs[0].metadata}')
print(type(docs[0]))