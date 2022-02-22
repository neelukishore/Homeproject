
class Human:

	def __init__(self,c,h):
		self.color=c
		self.height=h

	def run(self):
		print("running........")

	def walk(self):
		print("walking.......")

s1 = Human("white",8.9)
print(s1.color,s1.height)
s2 = Human("black",5.6)
print(s2.color,s2.height)
s3 = Human("red",7.8)
print(s3.color,s3.height)	
s1.run()
s1.walk()


		


