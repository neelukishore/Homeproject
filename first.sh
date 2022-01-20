#!/bin/bash

echo "This is my first program"
echo -e "Enter your name: \n"
read name
echo "Given name is : $name"
if [ $? -eq 0 ];then
	echo "success"
else
	echo "Fail"
fi
