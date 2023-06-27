import boto3
import io
import smart_open
import pickle


def load_df_pkl(bucket, key):
    url = "https://s3.us-east-2.amazonaws.com/{}/{}".format(
            bucket, key)
    with smart_open.open(url, 'rb') as f:
        df = pickle.loads(f.read())
    return df

def download_file_s3(bucket, file):
    '''download_file_s3
    Downloads a file from S3 and reads it.

    Args:
        client (:obj:`boto3.s3_client`): An S3 client
        bucket (str): S3 bucket
        file (:obj: `boto3.file_obj`): S3 file object

    Returns:
        (:obj:`io.BytesIO`): File object
    '''
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, file)
    return obj.get()['Body'].read()

def get_files_from_s3(bucket, folder, key_prefix=''):
    '''get_files_from_s3
    Gets multiple files from S3 given a bucket, folder and file prefix.

    Args:
        bucket (str): S3 bucket
        folder (str): S3 folder
        key_prefix (str): S3 file name prefix
    '''
    s3_client = boto3.client('s3')
    response = s3_client.list_objects(
        Bucket=bucket,
        Delimiter='/',
        Prefix='/'.join([folder, key_prefix])
    )
    files = response['Contents']
    for file in files:
        yield download_file_s3(s3_client, bucket, file)
