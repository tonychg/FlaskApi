#!/bin/bash
# Author      : github.com/TonyChG
# Date        : mer. 04 juil. 2018 15:37:36 CEST
# Version     : 0.0.1
# Description : Init docker on centos7

user="vagrant"
repo="https://download.docker.com/linux/centos/docker-ce.repo"

yum install -y -q epel-release
yum install -y -q docker-ce
yum install -y -q yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo "$repo"
yum install -y -q docker-ce
gpasswd docker -a "$user"
systemctl enable docker
systemctl start docker
ln -sfv '/var/lib/docker/volumes' '/root/volumes'
