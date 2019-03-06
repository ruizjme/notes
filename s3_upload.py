#!/usr/bin/env python

import boto3
import os
import glob
import sys

"""
Upload note content to S3 in order to serve it. Content includes:

    - Markdown notes (.md)
    - Images in assets/ (.png)

"""

def upload_static_content(bucket_name, file_list, target_dir='content'):
    '''Uploads all files in list to S3 bucket and makes them public'''
    s3 = boto3.resource('s3')

    content_type = {'md':'text/markdown; charset=utf-8',
                    'py':'text/x-python',
                    'css':'text/css',
                    'js':'application/javascript',
                    'json':'application/json',
                    'png':'image/png',
                    'gif':'image/gif',
                    'jpeg':'image/jpeg',
                    'jpg':'image/jpg',
                    'jpeg':'image/jpeg',
                    'pdf':'application/pdf',
                    }

    bucket = s3.Bucket(bucket_name)
    for file_name in file_list:
        file_ext = file_name.split('.')[-1].lower()
        file_target = os.path.join(target_dir.strip('/'), file_name.split('/').pop())
        bucket.upload_file(file_name, file_target,
                            ExtraArgs={'ContentType': content_type.get(file_ext,'text/plain'),
                                        'ACL': 'public-read'})

        print "{:40}{}".format(file_target, bucket.Object(file_target).content_type)

def list_files(source_dir='/Users/Jaime/Documents/BHERM/notes', extension='md'):
    files = glob.glob(source_dir+'/*.'+extension)
    return files

def list_files_in_bucket(bucket_name, prefix='static/img'):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    return [object.key for object in bucket.objects.filter(Prefix=prefix)]

# def make_bucket_public(bucket_name):
#     '''Makes entire bucket public'''
#     s3 = boto3.resource('s3')
#     bucket_acl = s3.BucketAcl(bucket_name)
#     response = bucket_acl.put(ACL='public-read')

# def list_all_objects(bucket_name):
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket(bucket_name)
#     return [obj.key for obj in bucket.objects.all()]

# def make_objects_public(bucket_name):
#     s3 = boto3.resource('s3')
#     all_obj = list_all_objects(bucket_name)
#     for obj_key in all_obj:
#         print obj_key
#         object_acl = s3.ObjectAcl(bucket_name, obj_key)
#         response = object_acl.put(ACL='public-read')

if __name__ == '__main__':
    BUCKET_NAME = 'notes-static-content'

    if len(sys.argv) > 1 and sys.argv[1] == 'css':
        files = list_files('/Users/Jaime/Documents/Development/Python/notes/static/css/', 'css')
        upload_static_content(BUCKET_NAME, files, target_dir='static/css/')

    else:
        # Upload MarkDown files
        files = list_files('/Users/Jaime/Documents/BHERM/notes/', 'md')
        upload_static_content(BUCKET_NAME, files, target_dir='content/')

        # Upload images
        local_files = [f.split('/').pop() for f in list_files('/Users/Jaime/Documents/BHERM/notes/assets/', '*')]
        cloud_files = [f.split('/').pop() for f in list_files_in_bucket(BUCKET_NAME, prefix='static/img/')]
        files = set(local_files) - set(cloud_files) # only upload images that are not yet in the bucket
        upload_static_content(BUCKET_NAME, files, target_dir='static/img/')
