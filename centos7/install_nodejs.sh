#!/bin/bash

yum install -y nodejs npm

# Set npm mirror registry
npm config set registry https://registry.npm.taobao.org
export PHANTOMJS_CDNURL=https://npm.taobao.org/mirrors/phantomjs
export SASS_BINARY_SITE=https://npm.taobao.org/mirrors/node-sass/

# Global requirements, run npm install
npm install -g n
PROJECT_NAME="node" PROJECT_URL="https://npm.taobao.org/mirrors/node/" n lts
