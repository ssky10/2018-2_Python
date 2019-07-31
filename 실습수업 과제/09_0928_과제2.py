num = int(input("정수를 입력하시오(5자리 이내):"))
sum = num%10
num //= 10
sum += num%10
num //= 10
sum += num%10
num //= 10
sum += num%10
num //= 10
sum += num%10
print("자리수의 합은",sum,"입니다.")
