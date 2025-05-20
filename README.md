# lag-local

## overview
lag is a typo of RAG


## setup
```shell
# 仮想環境の作成
$ python -m venv venv

# 仮想環境の有効化
$ source venv/bin/activate

# 必要なライブラリのインストール
$ pip install -r requirements.txt

# OPEN_AI_API_KEYの設定
$ export OPEN_AI_API_KEY="sk-xxxxxxxx"
```

## ドキュメントのダウンロード
```shell
$ python save_wiki.py
```

## ベクトルストアの作成
```shell
$ python create_vectorstore.py
```

## 質問の実施
```shell
$ python question.py
```

## jupyter notebookの起動
```shell
./venv/bin/jupyter notebook
```
