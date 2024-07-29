# dynamo_training_session
DynamoDB勉強会用

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

# 参考資料
- [boto3ドキュメント](https://boto3.amazonaws.com/v1/documentation/api/1.14.10/reference/services/dynamodb.html)
