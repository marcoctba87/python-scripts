import boto3
import json
index = 0
bundle = str(input("Informar o BundleID: "))

arq = open('criar.txt')
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

    response = client.create_workspaces(
        Workspaces=[
            {
                'DirectoryId': directory_id,
                'UserName': name,
                'BundleId': bundle,
                'WorkspaceProperties': {
                    'RunningMode': 'ALWAYS_ON',
                    'RootVolumeSizeGib': 80,
                    'UserVolumeSizeGib': 10,
                    'ComputeTypeName': 'PERFORMANCE'
                },
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Value'
                    },
                ]
            },
        ]
    )

    json_object = json.dumps(response, indent=2)

    print(json_object)

    arq.close()
