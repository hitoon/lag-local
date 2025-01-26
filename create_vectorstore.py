from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# テキストの読み込み
loader = TextLoader("output_wikipedia.txt")

# notionを読み込みたい場合
# from langchain.document_loaders import NotionDirectoryLoader
# ZIPでダウンロードしたファイルを解凍したディレクトリを指定
# loader = NotionDirectoryLoader("notion")

raw_docs = loader.load()
print(len(raw_docs))

# テキストの分割
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)
print(len(docs))

# ベクトルストアの保存
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # ローカルの保存場所
)

# ベクトル化はVector storeのクラスにデータを保存する際に内部的に実行される
vector_store.add_documents(documents=docs, embeddings=embeddings)

print("There are", vector_store._collection.count(), "in the collection")

# 以下のクエリに近いドキュメントを検索
query = "スミナガシート"
retriever = vector_store.as_retriever()
context_docs = retriever.invoke(query)
print(f"len = {len(context_docs)}")

first_doc = context_docs[0]
print(f"metadata = {first_doc.metadata}")
print(first_doc.page_content)
