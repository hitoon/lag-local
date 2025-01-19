from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# ベクトルストアの読み込み
# 保存したVector Storeのディレクトリ
persist_directory = "./chroma_langchain_db"

# 同じ埋め込み関数を使用
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Vector Storeを再ロード
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory=persist_directory,  # 保存先ディレクトリを指定
)

# コレクション内のドキュメント数を確認
print("There are", vector_store._collection.count(), "documents in the collection")


prompt = ChatPromptTemplate.from_template('''\
以下の文脈だけを踏まえて質問に回答してください。

文脈: """
{context}
"""

質問: {question}
''')

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

retriever = vector_store.as_retriever()

chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
)

output = chain.invoke("秩序の街に関して詳しく教えてください。")
# output = chain.invoke("スミナガシートはいつ追加されましたか？")
print(output)
