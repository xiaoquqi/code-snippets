# Step for k8s installation

## Common installation for both master and salve node

1. CentOS 7 installation: https://snippets.cacher.io/snippet/2d006af7464f93db5438
2. Docker installation: https://snippets.cacher.io/snippet/2db80b9676cfd593f716

## Master node
1. k8s basic installation
2. Initialization(Including network)

## Slave node
1. k8s basic installation
2. node join

# Useful Commnads

## Destroy cluster

    $ kubeadm reset
    
## Debug pods

    $ kubectl get pods --all-namespaces
    $ kubectl describe pod kubernetes-dashboard -n kube-system
    
## Get service

    $ kubectl -n kube-system get service kubernetes-dashboard
    
## Edit service config(Example: Access dashboard from master node ip)

    $ kubectl -n kube-system edit service kubernetes-dashboard
    
    Change type clusterIP to NodePort, save and exit
    
    [root@k8s ~]# kubectl -n kube-system get service kubernetes-dashboard
    NAME                   TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
    kubernetes-dashboard   NodePort   10.99.168.130   <none>        443:31800/TCP   31m

## Allow master to run pods

    $ kubectl taint nodes --all node-role.kubernetes.io/master-
    
## Assign external ip

I created a single node k8s cluster using kubeadm. When i tried PortForward and kubectl proxy, it showed external IP as pending.

$ kubectl get svc -n argocd argocd-server
NAME            TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
argocd-server   LoadBalancer   10.107.37.153   <pending>     80:30047/TCP,443:31307/TCP   110s
In my case I've patched the service like this:

kubectl patch svc <svc-name> -n <namespace> -p '{"spec": {"type": "LoadBalancer", "externalIPs":["172.31.71.218"]}}'
After this, it started serving over the public IP

$ kubectl get svc argo-ui -n argo
NAME      TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
argo-ui   LoadBalancer   10.103.219.8   172.31.71.218   80:30981/TCP   7m50s
