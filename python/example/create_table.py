import boto3

db_client = boto3.client(
    service_name="dynamodb",
    endpoint_url="http://dynamodb-local:8000",
    region_name="ap-northeast-1",
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy',
)

table_list = db_client.list_tables()["TableNames"]

print(table_list)

# Exampleテーブルがない場合は作成
if "Example" not in table_list:
    db_client.create_table(
        TableName="Example",
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
    )
    print("Exampleテーブルを作成しました。")

    db_client.put_item(
        TableName="Example",
        Item={
            "id": {"S": "test"},
        },
    )
else:
    print("Exampleテーブルはすでに存在します。")
