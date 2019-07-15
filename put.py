import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('staff')

table.put_item(
   Item={
		'username': 'nirbhay09',
		'first_name': 'Nirbhay',
		'last_name': 'Bagmar',
		'age': 20,
		'account_type': 'administrator',
	}
)