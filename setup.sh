#!/bin/sh
cd ~
git clone git@github.com:technocake/shoot-and-load.git -b marte

echo "alias sendbilder='. ~/shoot-and-load/shoot-and-load.py'" >> ~/.bash_aliases
