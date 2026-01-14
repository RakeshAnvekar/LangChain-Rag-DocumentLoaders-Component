# i have two books and i want to laod them using document loader
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader= DirectoryLoader(path='Books',glob='*.pdf',loader_cls=PyPDFLoader)


docs=loader.lazy_load()
print(len(docs))
