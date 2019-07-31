pie = 3.14

def Length(r):
    return 2*pie*r


def Area(r):
    return pie*(r**2)


r = int(input("원의 반지름을 입력하세요 : "))
while r <= 0:
    r = int(input("양수를 입력하세요 : "))

print("원의 둘레 : %.2f, 원의 넓이 : %.2f" %(Length(r),Area(r)))
