# Step2 initialization
# Specify kubernetes-version if mirror do not contain latest kubernetes container. ex: if kubeadm is version 1.18.5, you can only
# install kubernetes = 1.18.x
kubeadm init --pod-network-cidr=10.244.0.0/16 --image-repository registry.aliyuncs.com/google_containers --kubernetes-version=1.18.0
 
# Response from output
# You should now deploy a pod network to the cluster.
# Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
#   https://kubernetes.io/docs/concepts/cluster-administration/addons/
# Then you can join any number of worker nodes by running the following on each as root:
# kubeadm join 192.168.10.111:6443 --token 1odaru.0by05advhbu7edgt \
#     --discovery-token-ca-cert-hash sha256:3efb71c40cce36c5ed90fc8b5831233aba06eec26576088e8e7a7a892d272776
 
# Step3 flannel Network
sysctl net.bridge.bridge-nf-call-iptables=1
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# Step4 To use cluster
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
