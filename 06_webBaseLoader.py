from langchain_community.document_loaders import WebBaseLoader


from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()



model= ChatOpenAI()

parser= StrOutputParser()

prompt= PromptTemplate(

    template="answer the following question:\n{question}\n from  the following text \n{text}", 
    input_variables=["text","question"],     
)


loader= WebBaseLoader('https://www.flipkart.com/google-pixel-10-frost-256-gb/p/itm180af25bcc197?pid=MOBHEXHRXDGMF8XZ&lid=LSTMOBHEXHRXDGMF8XZ4R1W9O&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=CLP_Filters&fm=organic&iid=en_gHP5xdVGxa2Rtfe9LXszqYWW8A2UZXzefQwzv9E81COZ5kMdqnjDiunvIjFykHf4kDxJQPgFUk0p1iWRC5IKtg%3D%3D&ppt=clp&ppn=mobile-phones-store&ssid=6tbcagh81s0000001768371975201')
docs = loader.load()


chain=  prompt | model | parser

result= chain.invoke({'text': docs[0].page_content,'question':'What is the price of Google Pixel 10?'})

print(f'Answer Result:\n{result}')