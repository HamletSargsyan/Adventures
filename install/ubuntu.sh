#! /bin/bash

url="https://www.github.com/HamletSargsyan/Adventures/realeses/latest/archive/" # TODO

sudo apt install wget python3 python-pip

wget $url | tar

