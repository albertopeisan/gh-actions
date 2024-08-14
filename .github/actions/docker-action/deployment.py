import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    bucket = os.environ['bucket']
    bucket_region = os.environ['dist-folder']
    dist_folder = os.environ['bucket-region']

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'website-url=localhost:8000', file=fh)

    print(f'bucket: {bucket}, region: {bucket_region}, folder: {dist_folder}')

if __name__ == '__main__':
    run()
