#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import logging
import os
import sys

import oss2
from oss2.models import BucketWebsite

AK = "<access key>"
AS = "<access secret>"
BUCKET = "hypermotion-license"
REGION_URL = "http://oss-cn-beijing.aliyuncs.com"

logging.basicConfig(
    format="%(asctime)s %(process)s %(levelname)s [-] %(message)s",
    level=logging.INFO)

current_path = os.path.dirname(os.path.abspath(__file__))
webpages_path = os.path.join(current_path, "webpages")
logging.info("Webpages path is: %s" % webpages_path)

auth = oss2.Auth(AK, AS)
bucket = oss2.Bucket(auth, REGION_URL, BUCKET)

bucket.put_bucket_website(BucketWebsite('index.html', 'error.html'))

upload_files = glob.glob(os.path.join(webpages_path, "*"))
for upload_file in upload_files:
    if os.path.isfile(upload_file):
        logging.info("Uploading file %s..." % upload_file)
        filename = os.path.basename(upload_file)
        with open(upload_file, "rb") as fileobj:
            bucket.put_object(filename, fileobj)
        logging.info("Upload file %s successfully." % upload_file)
