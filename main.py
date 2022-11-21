import boto3

dms = boto3.client('rds')

response = dms.describe_db_instances()

#print(response)

for i in response["DBInstances"]:
    print(i["DBInstanceIdentifier"])
    print(i["DBInstanceStatus"])
    print("\n")
    # if (i["DBInstanceStatus"]=="available"):
    #     dms.stop_db_instance(DBInstanceIdentifier=i["DBInstanceIdentifier"])

#for dbinst in response:
#    print()