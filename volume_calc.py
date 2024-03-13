from decimal import Decimal

x = float(input("가로길이:"))
y = float(input("세로길이:"))
z = float(input("높이:"))

Vol = x*y*z
DecVol = Decimal(str(x)) * Decimal(str(y)) * Decimal(str(z))

print("박스의 넓이는(by Float):" + str(Vol) + "입니다.")
print("박스의 넓이는(by Decimal):" + str(DecVol) + "입니다.")
print("volume_calc2.py도 확인해주세요")

