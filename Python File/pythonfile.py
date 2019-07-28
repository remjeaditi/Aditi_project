import boto3
import time
l=["Namenode","Datanode1","Datanode2"]
p={}
client = boto3.client('ec2',region_name='us-east-1')
response = client.describe_instances()
				
for r in response['Reservations']:
	for i in r['Instances']:
		for j in i['Tags']:
			if j[u'Key']=="Name":
				p[j[u'Value']]=i['PrivateDnsName']
				
p1={}				
for i in p:
	if i in l:
		p1[i]=p[i]
print(p)
