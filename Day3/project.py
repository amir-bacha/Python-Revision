class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def ShowComplex(self):
        print(self.real,"i + ",self.imaginary,"j")

    def  __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.imaginary+num2.imaginary
        return Complex(newReal,newImg)
num1=Complex(4,5)
num2=Complex(6,7)
num1.ShowComplex()
num2.ShowComplex()
num3=num1+num2
num3.ShowComplex()