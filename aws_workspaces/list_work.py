import boto3
import json
index = 0

arq = open('arquivo.txt')
texto = [line.strip() for line in arq.readlines()]
directory_id = ''

for name in texto:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(index)
    print(texto[index])
    index = index + 1
    client = boto3.client('workspaces',
            aws_access_key_id='',
            aws_secret_access_key='',
            region_name='us-east-1'
            )

    response = client.describe_workspaces(
    		DirectoryId=directory_id,
    		UserName=name,
	)

    json_object = json.dumps(response, indent=2)

    print(json_object)

    arq.close()
