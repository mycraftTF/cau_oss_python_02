class Dec:
    exp = 0
    scaledVal = 0
    def getVar(self, Var):
        self.Var = Var

    def init(self):
        while self.exp >= 0:
            if float(self.Var)*(10**self.exp) % 1 == 0:
                self.scaledVal = float(self.Var)*(10**self.exp)
                self.scaledVal = int(self.scaledVal)
               # print(self.exp)
                break
            else:
                self.exp += 1

        #print(str(self.exp))
        #print(self.scaledVal)
    def mult():
        pass

x = Dec()
y = Dec()
z = Dec()

x.getVar(input("가로 길이:"))
x.init()
y.getVar(input("세로 길이:"))
y.init()
z.getVar(input("높이:"))
z.init()

scaledAns = x.scaledVal * y.scaledVal * z.scaledVal
totalExp = x.exp + y.exp + z.exp



#finAns = scaledAns * (10**-totalExp) 

lst = []

for i in str(scaledAns):
    lst.append(i)

print(len(lst))
lst.insert(len(lst)-totalExp, '.')

print(lst)


result = ''.join(str(s) for s in lst)

print(result)
