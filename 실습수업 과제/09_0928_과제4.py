import time
fsecond = time.time()
y = 1970 + ((fsecond)//(60*60*24*365))
print("현재 연도 : %d입니다." %y)
age = int(input("올해는 몇살인가요? "))
print("2050년에는 %d살 입니다." %(age+(2050-y)))