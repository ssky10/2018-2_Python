def Gender(code):
    code = int(code)%2
    if code == 0:
        return "여자"
    else:
        return "남자"


name = input("이름을 입력하세요 : ")
birth = input("주민등록번호 앞 7자리를 입력하세요 : ")
print("%s님은 %s월 %s일 출생으로, %s입니다" %(name,birth[2:4],birth[4:6],Gender(birth[-1:])))
