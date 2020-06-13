import os
from boto.s3.connection import S3Connection

API_KEY = S3Connection(os.environ['API_KEY'])