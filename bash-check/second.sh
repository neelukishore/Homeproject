#!/bin/bash

echo  -e  "enter the first string name: \c"
read -r string1
echo -e "enter the second string name: \c"
read -r string2
if [ $string1 == $string2 ]
then
	echo "both the strings are equal"
else
	echo "not equal"
fi
		
		