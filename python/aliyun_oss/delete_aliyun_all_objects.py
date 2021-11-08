#!/usr/bin/env python
# -*- coding: utf-8 -*-

import oss2

access_key_id = "xxxx"
access_key_secret = "xxxx"
endpoint = "oss-cn-beijing.aliyuncs.com"
bucket_name = "ray-s3-testing"

auth = oss2.Auth(access_key_id, access_key_secret)

bucket = oss2.Bucket(auth, endpoint, bucket_name)

is_truncated = True
next_marker = ""

while is_truncated:
    result = bucket.list_objects(
        prefix="", marker=next_marker, max_keys=1000)
    is_truncated = result.is_truncated
    next_marker = result.next_marker

    oss_objects = result.object_list

    will_del_objects = [obj.key for obj in oss_objects]
    print "Will delete objects: %s” % will_del_objects
    bucket.batch_delete_objects(will_del_objects)
