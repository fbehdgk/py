#함수 : 최소한의 기능을 하는 코드의 집합
#print type int float str

# 5 + 3의 타입을 확인하십시오
print(type("5+3"))

#최대값 구하기
a = max(3,5,312)
print(a)

#최소값 구하기
b = min(10,20)
print(b)

#합 구하기 iterable (반복가능하게) 값을 넣어야함
c = sum([10, 30])
print(c)

#3,7,10 중 가장 큰 값을 출력
print(max([3,7,10]))

#3과 7 중큰값을 10에 더해 합계를출력
print(sum([10, max(3,7)])) #1
print(max(3,7) + min(10,20)) #2

#기존 언어 내장된 함수의 사용법이나 언어의 사용법은 제작자의 맘

