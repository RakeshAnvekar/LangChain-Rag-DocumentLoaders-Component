from langchain_community.document_loaders import  CSVLoader

loader= CSVLoader('employee_master_data.csv')

docs=loader.load()
print(f'Number of documents loaded: {len(docs)}')
print(f'Content of the first document:\n{docs[0].page_content}')
print(f'Metadata of the first document:\n{docs[0].metadata}')