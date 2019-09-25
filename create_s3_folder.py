import boto3
s3 = boto3.client('s3')
bucket_name = "test-leo010"
for i in range(100000):
	directory_name = "year="+str(i).zfill(6) #it's name of your folders
	s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
	print i