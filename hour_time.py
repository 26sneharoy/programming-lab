class time:
    __hour=0
    __minute=0
    __second=0
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s
    def condition(self):
        if self.__second>=60:
            self.__second-=60
            self.__minute+=1
        if self.__minute>=60:
            self.__minute-=60
            self.__hour+=1
    def __add__(self,other):
        self.__hour=self.__hour+other.__hour
        self.__minute=self.__minute+other.__minute
        self.__second=self.__second+other.__second
        return (self.__hour,self.__minute,self.__second)
t1=time(3,45,57)
t2=time(4,55,45)
tt=(t1+t2)
tt.condition()
print("sum of the given time is : ",tt.condition())
print(tt)



        