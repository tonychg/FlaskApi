# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.provision "install", type: "shell", run: "once",
    :path => "./install-docker.sh"
end

