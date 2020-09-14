#!/bin/bash

username=$(sed "1q;d" .token)
api_key=$(sed "2q;d" .token)

if test -f "./.token"; then
    if test -z $username || test -z $api_key; then
        printf "\n\n\nCredentials missing.\n\n\n"
        exit 1
    fi
    echo "Removing files..."
    rm -rf ./dist ./build ./pymodorino.egg-info 

    echo "Packaging and building..."
    python setup.py sdist bdist_wheel

    echo "Uploading..."

    echo "Credentials= ${username} ${api_key}"
    expect -c "
    spawn twine upload dist/*
    expect \"Enter your username:\" { send \"${username}\r\"}
    expect \"Enter your password:\" { send \"${api_key}\r\"}
    expect eof"
else
    printf "\n\n\nNo .token file found.\n
Create a .token file with __token__ as first line and the api key on the second.
(+ an empty third line)\n\n\n"
fi