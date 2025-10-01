# Secure-S3-using-localstack
A personal project exploring secure file storage in AWS S3 using LocalStack. I practice server-side encryption, versioning, bucket policies, and presigned URLs locally, learning S3 security hands-on without touching real AWS resources.
I'm using Window by the way so I did it with window powershell remember to run it as administrator to be able to install Localstack and AWS CLI

---

## Features

- Create an S3 bucket in LocalStack
- Enable **server-side encryption (AES256)**
- Enable **versioning** for object protection
- Upload files to the bucket
- Apply **bucket policies** to restrict access
- Generate **presigned URLs** for temporary secure file sharing
- List bucket contents to verify uploads

---

## Project Structure
secure-s3-localstack/
│
├─ example.txt # Example file to upload
├─ s3_secure_project.py # Python automation script
├─ README.md # Project documentation
├─ requirements.txt # Python dependencies (boto3)
├─ json/ # JSON files for policies & versioning
│ ├─ bucket-policy.json
│ └─ versioning.json

---

## Setup Instructions

1. **Install prerequisites:**
   - [Python 3.x](https://www.python.org/downloads/)
   - [LocalStack](https://localstack.cloud/) (`pip install localstack`)
   - [AWS CLI](https://aws.amazon.com/cli/) (`pip install awscli`)
   - [Boto3](https://boto3.amazonaws.com/) (`pip install boto3`)
   - Optional: some machine require Docker to be able to run the Localstack, so for more information about it you can go in here https://www.docker.com/products/docker-desktop/

2. **Start LocalStack:**

```powershell
localstack start -d
aws configure
# Use dummy credentials:
# AWS Access Key ID: test
# AWS Secret Access Key: test
# Default region name: us-east-1
# Default output format: json

```
## Usage

Run the automation script:

python s3_secure_project.py


The script will:

- Create the bucket

- Enable server-side encryption

- Enable versioning

- Upload a file (example.txt)

- Apply a bucket policy

- Generate a presigned URL valid for 1 hour

- List the bucket contents

Notes

The project runs entirely on LocalStack, so no real AWS charges occur.

You can modify FILE_TO_UPLOAD in the script to test with different files.

Presigned URLs allow temporary access without changing bucket permissions.

## Screenshot of how the URL should show
<img width="963" height="462" alt="image" src="https://github.com/user-attachments/assets/c852d84e-e407-4b22-bf35-b7637283ac55" />

<img width="1800" height="603" alt="image" src="https://github.com/user-attachments/assets/de036683-f767-4f56-aea9-34d52b8d76b8" />
