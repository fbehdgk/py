# 두 숫자를 입력받아 큰 수를 가리는 함수
#                '''def is_big(num : int,num2):
'''                if num >num2:
                    return True
                elif num < num2:
                    return False
                elif num == num2:
                    print('같다')
                else : print('비교 불가능')
            int1 = int(input('숫자1입력'))
            int2 = int(input('숫자2입력'))
                #is_big(int1,int2)
                #if True:
                    #print('크다')'''


#숫자를 입력받아 절대값 계산 함수
def make_abd(num):
    return abs(num)
    
number = int(input('숫자입력'))
print(make_abd(number))

def make_abs(a):
    if a<0:
        return -a
    return a
number = int(input('숫자입력'))
print(make_abs(number))
