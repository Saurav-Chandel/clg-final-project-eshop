# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_dev"),)
import datetime
AWS_ACCESS_KEY_ID = "AKIAQS6B3M3MBOGCIVOI"
AWS_SECRET_ACCESS_KEY = "ulQ7XXgglZ3tfPPBYoc4AGezDRC+Yeh/nUH6JRHR"
AWS_FILE_EXPIRE=200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_S3_REGION_NAME = "us-east-1"  # e.g. us-east-2
AWS_STORAGE_BUCKET_NAME = "e-shop-django"
AWS_DEFAULT_ACL=None
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME   
# AWS_S3_CUSTOM_DOMAIN = "d2dr6wwncpi0to.cloudfront.net"
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": "max-age=86400",
# }
# AWS_LOCATION = "static"
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = "main.aws.utils.StaticRootS3BotoStorage"
DEFAULT_FILE_STORAGE = "main.aws.utils.MediaRootS3BotoStorage"

AWS_S3_SIGNATURE_VERSION="s3v4"

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 

# AWS_S3_FILE_OVERWRITE = False
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static_cdn"),)