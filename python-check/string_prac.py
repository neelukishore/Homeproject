#!/usr/bin/python


#### this is for string prac
###  https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2

#message = 'Bobby\'s world'
message = """ hey this is neelu\'s 
first project on python
"""
print(message)

message1 = 'hey neelu'
# print(message1[0:5])
# print(message1[-1])
# print(message1[-5])
# print(message1[::-1])
# print(message1.lower())
# print(message1.title())
# print(message1.rsplit())
# print(message1.split())
# message2 = 'hey hari '
# print(message2.rstrip())
# print(message2.strip())

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
y = txt.rstrip(".r")
print(y)
z = txt.rstrip(",.grt")
print(z)
