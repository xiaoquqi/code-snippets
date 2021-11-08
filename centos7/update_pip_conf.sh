#!/bin/bash
 
mkdir -p ~/.pip
tee ~/.pip/pip.conf << EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
 
[install]
trusted-host=mirrors.aliyun.com
EOF
