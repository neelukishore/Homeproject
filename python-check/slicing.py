#/usr/bin/python

sample_url='https://google.com'
print(sample_url)

############Reverse the url
print(sample_url[::-1])

########get the top level domain
print(sample_url[-4:])

#######print the url without https
print(sample_url[8:])

######without the https and top level domain
print(sample_url[8:-4])