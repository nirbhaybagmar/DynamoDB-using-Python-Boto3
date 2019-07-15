import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('staff')

table.delete_item(
	Key={
		'username': 'nirbhay09',
		'last_name': 'Bagmar'
	}
)