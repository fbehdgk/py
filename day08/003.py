#예외(Exception) : 실행중 발생하는 오류
#예외 처리 : 예외가 발생시 오류 메시지를 내고 정상 종료하게 하는것
# try: 예외가 발생할 수 있는 코드 except:
try:
    jumsu = int(input('점수입력'))
    if jumsu >=70:
        print('합격')
    else: print('불합격')
except:
    print('점수를 숫자로 입력하세요')
    