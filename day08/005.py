#나눗셈 결과를 리턴하는 함수
def divide(a:int,b:int):
    try:
        return a/b
    except:
        return '0으로 나눌수 없음'