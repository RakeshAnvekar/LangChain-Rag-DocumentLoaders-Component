from langchain_community.document_loaders import TextLoader

from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

loader= TextLoader('example.txt', encoding='utf8')
docs = loader.load()

model= ChatOpenAI()

parser= StrOutputParser()

prompt= PromptTemplate(

    template="Summarize the following text in 5 line:\n\n{text}", 
    input_variables=["text"],     
)

chain= prompt | model | parser


result= chain.invoke({'text': docs[0].page_content})
print(f'Summarization Result:\n{result}')