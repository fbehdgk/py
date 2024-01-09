numbers = [1,3,5,7]
#숫자가 numbers에 있는지 출력하시오 
num = 5
print(num in numbers)
#in을 쓰지 않기
print('----------------')
i = 0
for item in numbers:
    if item == num:
        print(True)
        i = 1
if i == 0:
    print(False)    