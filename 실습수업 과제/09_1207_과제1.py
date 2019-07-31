dic = {}

while True:
    key = input("(입력모드)이름을 입력하시오:")
    if key == "":
        break;

    dic[key]= input("전화번호를 입력하시오:")


while True:
    key = input("(검색모드)이름을 입력하시오:")
    if key == "":
        break;

    if key in dic.keys():
        print(key,"님의 전화번호는",dic[key],"입니다.")
    else:
        print(key,"님의 전화번호는 존재하지 않습니다.")

    
