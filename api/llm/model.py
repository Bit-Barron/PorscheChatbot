from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (SentenceTransformerEmbeddings)
from langchain_community.vectorstores import Chroma

loader = TextLoader('state_of_the_union.txt', encoding="utf-8")
