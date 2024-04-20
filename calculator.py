class Calculator:

    def __init__(self,num1,num2):
        self.value1 = num1
        self.value2 = num2

    def Addition(self):
        sum = self.value1 + self.value2
        print("sum = " , sum)
  
    def Subtraction(self):
        sub = self.value1 - self.value2
        print("sub = " , sub)

    def Multiplecation(self):
        multi = self.value1 * self.value2
        print("multi = " , multi)

    def Devision(self):
        devide = self.value1 / self.value2
        print("devide = " , devide)

    def Modulation(self):
        module = self.value1 % self.value2
        print("module = ", module)

    def Double_devision(self):
        d_devide = self.value1 // self.value2
        print("d-devide = " , d_devide)

    def Power(self):
        power = self.value1 ** self.value2
        print("power = " , power)

print("..............CALCULATOR..............\n\n")

while True :
  
    value1 = int(input("Enter first value....\n"))
    value2 = int(input("Enter second value....\n"))  

    print("display the option by user select this.....\n")
  
    print("1. for Addition(+) \n2. for subtraction(-)\n")
  
    print("3. for multiplecation(*) \n4. for Devision(/)\n")
  
    print("5. for modulation(%) \n6. for Double_devision(//)\n")
  
    print("7. for Power(**) \n\n")

    opt = int(input("Enter any option ... : 1,2,....7\n\n"))
  
    c1 = Calculator(value1,value2)

    if(opt == 1):
      c1.Addition()
      
    elif(opt == 2):
        c1.Subtraction()
      
    elif(opt == 3):  
        c1.Multiplecation()
    
    elif(opt == 4):
        c1.Devision()
    
    elif(opt == 5):
        c1.Modulation()
    
    elif(opt == 6):
        c1.Double_devision()
    
    elif(opt == 7):
        c1.Power()
    else:
      while(opt>7):
        print("number is default please try again:,,,,  ")

    print("THANK YOU ...")    

    print("do you wnat to agin calculate value:.....\n")
  
    if(input("yes or no:.....") == "yes"):
       continue
    else:
       print("you are exit from the calculator...")
       break


   