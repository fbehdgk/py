import e005

from e005 import hello
from e005 import print_py

e005.hello()
print_py()


def message():
    print("A")
    print("B")

#함수는 동시에 실행되지않는다(한번에 하나씩만 실행)
#병렬 프로그래밍 : 함수 동시실행(난이도가 높음 순서대로 돌아가야하는데 한번에 돌아가니까 작업순서에 문제가 생길수 있음 따라서 보통 사용안함)
# 근데 자바스크립트는 병렬프로그래밍되니까 직접 순서를 맞춰야한다 
#서버와 통신하는 코드는 모두 병렬프로그래밍이다 
'''
챔피언정보 = fetch('LOL주소')
print(챔피언정보) 
console.log("aaaa") 
---
이렇게 하면 나오는 결과는 챔피언정보부분이 null
aaaa 만 출력된다 
따라서 우리는 awate anc? 로 순서를 정해서 실행되게 해야한다
'''
message()
print("C")
message()
