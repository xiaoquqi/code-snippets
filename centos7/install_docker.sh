# Install Docker
curl -sSL https://get.daocloud.io/docker | sh -s -- "--mirror" "Aliyun"

# Replace docker repo
mkdir -p /etc/docker
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": ["https://6m7d428u.mirror.aliyuncs.com"],
  "dns": ["114.114.114.114"],
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
EOF
 
systemctl enable docker && systemctl daemon-reload && systemctl restart docker

curl -L http://mirrors.aliyun.com/docker-toolbox/linux/compose/1.21.0/docker-compose-Linux-x86_64 > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
