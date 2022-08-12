#!/bin/bash

#Type your Login Credentials

read -p 'Username :' user
read -sp 'Password :' pass

if (($user == "amruth" && $pass == "434123"))
then
echo -e "\nWelcome ! LOGIN SUCCESSFUL\n"
else
echo -e "\nLOGIN UNSUCCESSFUL\n"
fi
