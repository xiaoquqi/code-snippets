#!/bin/bash
 
 
# Set SELinux in permissive mode (effectively disabling it)
setenforce 0
#sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
sed -i 's/^SELINUX=enforcing$/SELINUX=disabled/' /etc/selinux/config
 
systemctl stop NetworkManager
systemctl disable NetworkManager
 
systemctl status firewalld
systemctl stop firewalld
systemctl disable firewalld
systemctl status firewalld
firewall-cmd --state
 
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum clean all && yum makecache
yum update -y
