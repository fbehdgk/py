def sample(a:int): # 인자가 뭐가 와야하는지에 대한 가이드 라인일뿐 밑에거 다 통과 됨 
    print(a)

sample(10)
sample('hello')

#정수 2개를 인자로 받아 덧셈 후 출력하는 함수를 정의하고 호출
def aa(a:int | float,b:int | float):
    print(a+b)

aa(1,2)

def aa2(a:int | float,b:int | float):
    #return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a+b
result = aa2(3,4)
print(aa2(3,4))
