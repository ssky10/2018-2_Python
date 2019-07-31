def sub(x,y):
    global a
    a = 7
    temp = x
    x = y
    y = temp
    b = 3
    print(a,b,x,y)

a = 1
b = 2
x = 3
y = 4

sub(x,y)
print(a,b,x,y)

"""
1. 결과 값
    sub(x,y) = 7 3 4 3
    print(a,b,x,y) = 7 2 3 4

2. 각 변수들의 변화값
    1)sub(x,y)
    a : 1 -> 7
    b : 2 -> 3
    x : 3 -> 4
    y : 4 -> 3

    2)print(a,b,x,y)
    a : 1 -> 7(sub에서 변경)
    b : 2
    x : 3
    y : 4

3. 결과값이 왜 이렇게 출력되는가?
    전역변수로써 a,b,x,y를 각각 1,2,3,4를 생성하고 나서
    sub(x,y)를 호출한 경우 sub내부의 a는 global 키워드로 인해
    전역 변수 a를 지칭하게 되고 그외의 b,x,y는 지역변수를 별도로 생성하게 된다.
    따라서 sub에서 값을 변경하였을때 전역변수인 a를 제외한 나머지 변수들은
    지역변수임으로 sub를 벗어났을때 영향력이 미치지 않으며,
    sub바깥의 print에서는 전역변수인 a,b,x,y를 의미하므로 결과값이 서로 다르게 나타난다.
    sub(x,y) -> a:전역변수 / b,x,y:지역변수
    print(a,b,x,y) -> a,b,x,y:전역변수
"""