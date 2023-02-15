import boto3

# Create a client to interact with DynamoDB
dynamodb = boto3.client('dynamodb')

# Create a new table with a partition key
table_name = "example_table"
partition_key_name = "example_partition_key"
try:
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                "AttributeName": partition_key_name,
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": partition_key_name,
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:", e)

# Add three items to the table
try:
    response = dynamodb.batch_write_item(
        RequestItems={
            table_name: [
                {
                    "PutRequest": {
                        "Item": {
                            partition_key_name: {
                                "S": "item1"
                            },
                            "other_attribute": {
                                "S": "value1"
                            }
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            partition_key_name: {
                                "S": "item2"
                            },
                            "other_attribute": {
                                "S": "value2"
                            }
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            partition_key_name: {
                                "S": "item3"
                            },
                            "other_attribute": {
                                "S": "value3"
                            }
                        }
                    }
                }
            ]
        }
    )
    print("Items added successfully!")
except Exception as e:
    print("Error adding items:", e)

# Delete an item from the table based on the partition key
try:
    response = dynamodb.delete_item(
        TableName=table_name,
        Key={
            partition_key_name: {
                "S": "item2"
            }
        }
    )
    print("Item deleted successfully!")
except Exception as e:
    print("Error deleting item:", e)
