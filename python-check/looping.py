####using enumerate

for key,value in enumerate(['the', 'big', 'theory']):
	print(key, value)

for key, value in enumerate(['my', 'name', 'is', 'riyan']):
	print(value, end=' ')

#########using zip

name1 = ['name', 'colour', 'shape']
name2 = ['apple', 'red', 'a circle']

for name1, name2 in zip(name1, name2):
	print('\nWhat is your {0}?  I am {1}.'.format(name1, name2))

########using items()

king = {'Akbar': 'The Great', 'Chandragupta': 'The Maurya',
        'Modi': 'The Changer'}

for key, value in king.items():
	print(key, value)


#########using sorted()

lis = [1, 3, 5, 6, 2, 1, 3]

print("The list in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")
 
print("\r")

# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.

print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
    print(i, end=" ")



###########using reversed()

lis = [1, 3, 5, 7, 9, 1, 3]

print("\n the list in reversed order is :")
for i in reversed(lis):
	print(i, end=" ")

# Numbers from 10 to 15
# start = 10
# stop = 50
# step = 5
for i in reversed(range(10,20,3)):
	print(i)











