#/usr/bin/python

f = open('first.sh','r')

wf =open('first_copy.sh','w')

for line in f:

        wf.write(line) 

#print(f.name)

#print(f.mode)

#print(f.closed)

#print(f.read())

#print(f.readlines())

#size_to_read = 10

#f_contents = f.read(size_to_read)

#print(f_contents,end='')

#f.seek(0)

#f_contents = f.read(size_to_read)

#print(f_contents,end='')

#for line in f:
#	print(line,end='*')

f.close()