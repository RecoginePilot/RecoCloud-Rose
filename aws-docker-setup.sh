#!/bin/bash

## Docker Version Control
D_VER="5:20.10.24~3-0~ubuntu-jammy"
echo "Welcome to the AWS Docker Setup Script"

## Intsall
function INSTALL() {
    sudo mkdir -m 0755 -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ## Optional Upgrade
    #sudo apt-get upgrade -y
    sudo apt-get install -y bash-completion htop tmux curl
    sudo apt-get install -y gnome-terminal ca-certificates curl gnupg lsb-release docker-ce=${D_VER} docker-ce-cli=${D_VER} containerd.io
    sudo usermod -aG docker $USER
    sudo curl -L -o /usr/local/bin/docker-compose \
    "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)"
    sudo curl -L -o /etc/bash_completion.d/docker-compose \
    https://raw.githubusercontent.com/docker/compose/1.29.2/contrib/completion/bash/docker-compose \
    -o /etc/bash_completion.d/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
}


## Uninstall
function REMOVE () {
    sudo apt purge docker docker-engine docker.io containerd runc docker-desktop
    rm -r $HOME/.docker/desktop
    sudo rm /usr/local/bin/com.docker.cli /etc/apparmor.d/docker
    sudo rm -rf /var/lib/docker /etc/docker /var/run/docker.sock /usr/bin/docker-compose /var/lib/containerd
    sudo groupdel docker
}

INSTALL;
