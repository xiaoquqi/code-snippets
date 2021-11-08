#!/bin/bash

curl -O https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml
sed -i 's/k8s.gcr.io/registry.cn-hangzhou.aliyuncs.com\/google_containers/' kubernetes-dashboard.yaml

# Add following lines
# ------------------- Dashboard Service ------------------- #
#kind: Service
#apiVersion: v1
#metadata:
#  labels:
#    k8s-app: kubernetes-dashboard
#  name: kubernetes-dashboard
#  namespace: kube-system
#spec:
#  type: NodePort
#  ports:
#    - port: 443
#      targetPort: 8443
#      nodePort: 30001
#  selector:
#    k8s-app: kubernetes-dashboard

kubectl create -f kubernetes-dashboard.yaml

kubectl get pods -n kube-system

# kubernetes-dashboard-86844cc55f-flmk7   1/1     Running   0          23s
