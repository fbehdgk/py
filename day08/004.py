# 정수 변수 2개를 만들어 나눗셈 결과 출력
#예외처리필요시 예외처리
int1 = int(input('정수1입력'))
int2 = int(input('정수2입력'))
ft = False
def div(num1,num2):
    try:
        return  num1/num2, ft == True
    except: 
        num2 == 0
    finally:
        print('0으로 못나눔')

num3 = div(int1,int2)
if ft == True:
    print(f'값:{num3}')
'''잘못만든코드임'''