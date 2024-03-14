import functools as ft


class Dec:      #소수점으로 입력받아 소수점 자릿수와 변환된 수(12.3 -> 123) 저장
    exp = 0
    scaledVal = 0

    def getVar(self, Var):
        self.Var = Var

    def init(self):
        while self.exp >= 0:
            if float(self.Var)*(10**self.exp) % 1 == 0:        #입력받은 소수에 10의 n승을 곱하고 1로 나눠 나머지가 없을시 정수로 판단, n을 소수점 자릿수로 판단
                self.scaledVal = float(self.Var)*(10**self.exp)
                self.scaledVal = int(self.scaledVal)
               # print(self.exp)
                break
            else:
                self.exp += 1


def decDigit(number, exponential):      #정수형 수와 소수점 자릿수를 입력받아 소수점을 붙인뒤 반환
    list = []
    for i in str(number):       #인자로 받은 정수를 리스트로 변환
        list.append(i)

    list.insert(len(list) - exponential, '.')       #리스트에서 소수점이 있어야할 부분에 소수점을 삽입
    ans = ''.join(str(s) for s in list)
    ans = float(ans)
    return ans

def multDec(a, b, c):       #Dec으로 된 객체 3개를 인자로 넘겨받아 곱한 뒤 반환
    sAns = a.scaledVal * b.scaledVal * c.scaledVal
    print(sAns)
    totExp = a.exp + b.exp + c.exp

    return decDigit(sAns, totExp)




def main():
    x = Dec()
    y = Dec()
    z = Dec()

    x.getVar(input("가로 길이:"))
    x.init()
    y.getVar(input("세로 길이:"))
    y.init()
    z.getVar(input("높이:"))
    z.init()

    print("박스의 부피는:" + str(multDec(x, y, z)) + "입니다.")
    


if __name__== "__main__":
    main()

