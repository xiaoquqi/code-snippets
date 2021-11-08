#!/bin/bash

curl -Lo minikube http://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/releases/v1.2.0/minikube-darwin-amd64 && \
          chmod +x minikube && sudo mv minikube /usr/local/bin/

minikube start --registry-mirror=https://registry.docker-cn.com

# Specify version
#minikube start --registry-mirror=https://registry.docker-cn.com --kubernetes-version v1.12.1
