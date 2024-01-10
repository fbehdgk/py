'''
# 1부터 10까지 합
result = 0
for a in range(1,11):
    result= result+a
print(result)
# 1부터 10까지 3의 배수 합
print('--------')
result = 0
for a in range(1,11):
    if a%3 ==0 :
        result= result+a
print(result)
print('--------')
result = 0
for a in range(1,11):
    if a%3 !=0 :
        continue # 스킵
    #result= result+a
    print(a)
'''
#1에서 10사이의 3의 배수 합계
print('--------')
result = 0
for a in range(1,11):
    if a%3 ==0 :
        result= result+a
print(result)

#1에서 100사이의 3과 5의 공배수 합계
print('--------')
result = 0
for a in range(1,101):
    if a%7 ==0 and a%5 == 0:
        #result= result+a
        print(a)
#1에서 100사이의 7과 5의 배수 출력 그러나 공배수제외
print('--------')
result = 0
for a in range(1,101):
    if (a%7 ==0 or a%5 == 0 ) != (a%7 ==0 and a%5 == 0 ) :
        print(a)

    

