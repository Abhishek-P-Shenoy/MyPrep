'''

We are creating a cookie cutter.

'''


class Cookie:
    #This is a constructure
    def __init__(self,color):
        self.color = color
    
    #This are fucntions in the class
    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color =color

'''
we have defined the cookie now we need the instent of the class so we need to call the name again with the redured parameters
'''

Cookie1 = Cookie("black")

print(Cookie1.get_color())
Cookie1.set_color("blue")
print(Cookie1.get_color())