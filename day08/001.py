#나이를 입력받아 성년 또는 미성년을 리턴하는 함수
def is_adult(nai : int): #질문형 함수의 경우 is로 시작하는 경우가 많음
    #nai = int(input('나이를 입력하시오 :'))
    if nai >=18 : 
        return '성년'
    else:return '미성년'
if is_adult(25) == '성년':
    print('출입가능')
else : print('되겠냐?')
