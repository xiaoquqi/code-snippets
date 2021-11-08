# step1 Installation Process
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
exclude=kube*
EOF
 
# Set SELinux in permissive mode (effectively disabling it)
setenforce 0
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
 
yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
 
systemctl enable kubelet

# for CentOS 7
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
vm.swappiness=0
EOF
sysctl --system

# Step2 Join
# This information is commming from previous init command
kubeadm join 192.168.10.111:6443 --token 1odaru.0by05advhbu7edgt \
    --discovery-token-ca-cert-hash sha256:3efb71c40cce36c5ed90fc8b5831233aba06eec26576088e8e7a7a892d272776

# if this information is lost, we can also get information as following:
# 1. Generate new token
kubeadm token create
kubeadm token list
# 2. Get ca cert
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
# 3.join
kubeadm join 192.168.10.111:6443 --token <from step 1> \
    --discovery-token-ca-cert-hash sha256:<from step 2>
    
# Step3 Check node status
kubectl get nodes
