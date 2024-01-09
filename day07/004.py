numbers = [1,3,5,7]
#숫자가 numbers에 있는지 출력하시오 
num = 5
print(num in numbers)
#in을 쓰지 않기
print('----------------')
# 한번만 찾으면 성공한것이지만 실패는 모든 값을 확인해서 없을때 없는것
# 밑처럼 어떤 상황에 대해 어떠한 해결법을 제시하는것이 디자인패턴 코딩의 정석 패턴을 외워둬야한다
isFind = False
for item in numbers:
    if item == num:
        print(True)
        isFind = True
if isFind == False:
    print(False)    