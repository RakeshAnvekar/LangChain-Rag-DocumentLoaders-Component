from langchain_community.document_loaders import TextLoader

loader= TextLoader('example.txt', encoding='utf8')
docs = loader.load()

print(f'Number of documents loaded: {len(docs)}')

print(f'Content of the first document:\n{docs[0].page_content}')
print(f'Metadata of the first document:\n{docs[0].metadata}')

print(type(docs[0]))