from django.conf import settings
from django.core.files.storage import FileSystemStorage

from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION

class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False

if not settings.USE_S3_STORAGE:
    StaticStorage = FileSystemStorage
    PublicMediaStorage = FileSystemStorage
    PrivateMediaStorage = FileSystemStorage