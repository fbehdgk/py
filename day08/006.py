#for문
# 헬로를 for문을이용해서 3번 출력하시오
for x in (1,2,3)  :
    print('hello')
print('--------')
#range는 0부터 시작하는 범위 생성이라고 보면됨 즉 입력한수 - 1회 반복 밑은 2까지
for x in range(3):
    print(x)
print('--------')
# for을 이용해서 0~10까지 출력
for x in range(11):
    print(x)
print('--------')
# for을 이용해서 0~10까지 짝수 출력
for x in range(11):
    if x%2 == 0 and x !=0:
        print(x)
print('--------')
result = 0
for a in range(1,11):
    result= result+a
print(result)
