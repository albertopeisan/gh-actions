import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    bucket = os.environ['INPUT_BUCKET']
    bucket_region = os.environ['INPUT_BUCKET-REGION']
    dist_folder = os.environ['INPUT_DIST-FOLDER']

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'website-url=localhost:8000', file=fh)

    print(f'bucket: {bucket}, region: {bucket_region}, folder: {dist_folder}')

if __name__ == '__main__':
    run()
