class Parent:
    counter=10;
    def __init__(self):
        print("Parent Initialization....")
    def parentFunction(self):
        print("Parent Fucntion being called....")
    def setCounter(self,num):
        Parent.counter=num;
    def showCounterValue(self):
        print(" The Counter value is: "+ str(Parent.counter))

class Child(Parent):
    def __init__(self):
        print("Child  Initialzed......")
    def childFunction(self):
        print("Child Fucntion is being called....")


"This is Inheritance Example"
child= Child()
child.childFunction()
child.parentFunction()
print(child.counter)

child.setCounter(134)
print(child.counter)

