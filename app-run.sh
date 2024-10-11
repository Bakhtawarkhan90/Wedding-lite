#!/bin/bash

echo "*********************************************** Update the package index *******************************************"
sudo apt-get -y update

echo "*********************************************** Install Docker ***************************************************"
sudo apt-get install -y docker.io

echo "*********************************************** Install Docker Compose v2 ***************************************************"
sudo apt-get install docker-compose-v2


echo " Add the current user to the Docker group "
sudo usermod -aG docker $USER && newgrp docker

echo " Clone the repository "
git clone https://github.com/Bakhtawarkhan90/Wedding-lite.git

echo " Change into the repository directory "
cd Wedding-lite

echo " Build and run the Docker containers "
docker compose up --build -d

echo " Docker && Docker-Compose version "
docker --version
docker compose version

echo " Below Are The Running Docker Containers "
docker ps

echo "*********************************************** Now You Can Access The App On $(curl -s ifconfig.me):5000 ***************************************"
