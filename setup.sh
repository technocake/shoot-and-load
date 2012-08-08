#!/bin/sh
cd ~
git clone git@github.com:technocake/shoot-and-load.git -b marte

echo "alias sendbilder='python ~/shoot-and-load/shoot-and-load.py'" >> ~/.bash_aliases
. .bash_aliases

echo "Starting sendbilder :)"
sendbilder
echo "Setup has finished"

echo 
echo " To start it another time, just type this command in your terminal:"
echo "sendbilder"

echo "Robin loves Marte"
