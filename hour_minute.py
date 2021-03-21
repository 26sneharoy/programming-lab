class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__seconds=s
        
    def convert(self):
        if self.__seconds>=60:
            self.__seconds-=60
            self.__minute +=1
        if self.__minute>=60:
            self.__minute-=60
            self.__hour +=1
        return(self.__hour,self.__minute,self.__seconds)
    def __add__(self,other):
        print("Time1:",(self.__hour,self.__minute,self.__seconds))
        print("Time2:",(other.__hour,other.__minute,other.__seconds))
        
        self.__hour=self.__hour + other.__hour
        self.__minute=self.__minute + other.__minute
        self.__seconds=self.__seconds + other.__seconds
        return(self)
        

t1=Time(2,40,50)

t2=Time(9,45,55)

t3=(t1+t2)
print("Time1 + Time2:",t3. convert())