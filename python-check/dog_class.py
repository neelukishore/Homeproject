#/usr/bin/python

#### object oriented programming

class Dog:
  
    # class attribute
    attr1 = "mammal"
  
    # Instance attribute
    def __init__(self, name):
        self.name = name
          
    def speak(self):
        print("My name is {}".format(self.name))


def main():
    dog1 = Dog('ruby')
    dog2 = Dog('lucky')
    dog1.speak()
    dog2.speak()


if __name__ == '__main__':
    main()