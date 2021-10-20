#!/usr/bin/env bash

# update & upgrade
apt-get -y update
apt-get -y upgrade

# install vim
apt -y install vim

# install git
apt install -y git-all

# update & upgrade
apt-get -y update
apt-get -y upgrade

# install software properties common
apt-get -y install software-properties-common

# update & upgrade
apt-get -y update
apt-get -y upgrade

# install pip from python
apt -y install python3-pip

# update & upgrade
apt-get -y update
apt-get -y upgrade

# Install Django
pip install Django==3.2.8

# Install selenium
pip install selenium

# Install beautifulsoup4
pip install beautifulsoup4

# Install curl
apt-get -y curl

# update & upgrade
apt-get -y update
apt-get -y upgrade

#Install NodeJs
curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
apt-get install -y nodejs

# update & upgrade
apt-get -y update
apt-get -y upgrade

# Install mysql
apt -y install mysql-server
service mysql start
mysql --version

# Install mysql client for Django
apt-get -y install python-dev default-libmysqlclient-dev
apt-get -y install python3-dev
pip install mysqlclient
