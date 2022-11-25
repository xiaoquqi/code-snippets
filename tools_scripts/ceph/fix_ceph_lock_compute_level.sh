#!/bin/bash
computename=$1
if [[ "x$computename" == "x" ]]; then
    echo "$0 <compute201|compute202|compute203>"
    exit 1
fi
TODAY=$(date +%Y%m%d)
touch /root/computelist$TODAY.txt
# 生成虚拟机名称文件
openstack server list --host=$computename --all-projects -f value | awk '{print $2}' | while read -r Servername
do
echo $Servername >> /root/computelist$TODAY.txt
done
 
# 生成虚拟机rbd磁盘文件
cat computelist$TODAY.txt | while read -r Servername1
do
openstack volume list -f value --all-projects | grep $Servername1 | awk '{print $1}'| while read -r volume1
do
volume2=volume-$volume1
echo $volume2 >> /root/volumelist$TODAY.txt
done
done
 
# 执行ceph lock解除
cat /root/volumelist$TODAY.txt | while read -r volume3
do
rbd lock ls -p volumes $volume3 | grep client
if [ $? -eq 0 ]
then
client1=`rbd lock ls -p volumes $volume3 | awk '/client/ {print $1}'`
client2=`rbd lock ls -p volumes $volume3 | awk '/client/ {print $2,$3}'`
rbd lock remove volumes/$volume3 "$client2" $client1
fi
done
 
# 重启虚拟机
openstack server stop $(openstack server list --host=$computename -f value --all-projects | awk '{print $1}')
sleep 120
openstack server start $(openstack server list --host=$computename -f value --all-projects | awk '{print $1}')
