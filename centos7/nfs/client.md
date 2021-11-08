yum install -y nfs-utils

mkdir -p /mnt/nfs/var/nfsshare

mount -t nfs 192.168.0.100:/var/nfsshare /mnt/nfs/var/nfsshare/

Edit /etc/fstab

192.168.0.100:/var/nfsshare    /mnt/nfs/var/nfsshare   nfs defaults 0 0
