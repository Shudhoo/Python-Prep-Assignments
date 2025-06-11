import boto3

# Set your desired AWS region here (e.g., 'ap-south-1' for Mumbai)
region = 'ap-south-1'

# Create S3 client with region
client = boto3.client('s3', region_name=region)

# Create the bucket
response = client.create_bucket(
    Bucket='my-unique-bucket-name-shudho',  
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print("Bucket created successfully:", response)
