import boto3
from botocore.client import Config
import os
import json

#making sure that your locakstack is running before running this automation file
LOCALSTACK_ENDPOINT = "http://localhost:4566"
BUCKET_NAME = "my-secure-bucket"
FILE_TO_UPLOAD = "C:/User/Documents/example.txt"  # Change to your file path
PRESIGNED_URL_EXPIRATION = 3600  # seconds (1 hour)

# Create S3 client pointing to LocalStack
s3 = boto3.client(
    "s3",
    endpoint_url=LOCALSTACK_ENDPOINT,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    config=Config(signature_version="s3v4"),
    region_name="us-east-1"
)

# Create the bucket
try:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket '{BUCKET_NAME}' created.")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{BUCKET_NAME}' already exists.")

#  Enable Server-Side Encryption (AES256)
s3.put_bucket_encryption(
    Bucket=BUCKET_NAME,
    ServerSideEncryptionConfiguration={
        "Rules": [
            {
                "ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}
            }
        ]
    }
)
print("Server-side encryption enabled (AES256).")

# Enable Versioning

s3.put_bucket_versioning(
    Bucket=BUCKET_NAME,
    VersioningConfiguration={"Status": "Enabled"}
)
print("Versioning enabled.")

# Upload a file
file_name = os.path.basename(FILE_TO_UPLOAD)
s3.upload_file(FILE_TO_UPLOAD, BUCKET_NAME, file_name)
print(f"File '{file_name}' uploaded.")

#  Apply Bucket Policy (Deny all by default)
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": [
                f"arn:aws:s3:::{BUCKET_NAME}",
                f"arn:aws:s3:::{BUCKET_NAME}/*"
            ]
        }
    ]
}

s3.put_bucket_policy(Bucket=BUCKET_NAME, Policy=json.dumps(bucket_policy))
print("Bucket policy applied (deny all).")

# Generate Presigned URL
presigned_url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": BUCKET_NAME, "Key": file_name},
    ExpiresIn=PRESIGNED_URL_EXPIRATION
)
print(f"Presigned URL (valid 1 hour):\n{presigned_url}")

#  List objects to verify
objects = s3.list_objects_v2(Bucket=BUCKET_NAME)
if "Contents" in objects:
    print("Bucket contents:")
    for obj in objects["Contents"]:
        print(f" - {obj['Key']}")
else:
    print("Bucket is empty.")
