# dynamo_training_session
DynamoDb勉強会用

## 環境構築

```
docker network create dynamodb-network
docker compose up --build -d
```

## pythonスクリプト実行

```
docker exec -it python bash

python example/create_table.py
```
