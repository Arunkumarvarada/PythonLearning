class Super:
    def __init__(self):
        pass

    def function(self):
        print(" This is Super class function")


class Sub(Super):
    def function(self):
        print(" This is Sub class function")


c= Sub()
c.function()
super().function()