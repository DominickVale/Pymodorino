#!/bin/bash

echo "Removing files..."
rm -rf ./dist ./build ./pymodorino.egg-info 

echo "Packaging and building..."
python setup.py sdist bdist_wheel

echo "Uploading..."
username=$(sed "1q;d" .token)
api_key=$(sed "2q;d" .token)

echo "Credentials= ${username} ${api_key}"
expect -c "
spawn twine upload dist/*
expect \"Enter your username:\" { send \"${username}\r\"}
expect \"Enter your password:\" { send \"${api_key}\r\"}
expect eof"