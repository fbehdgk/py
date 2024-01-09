numbers = [] # 이 배열을 밖에 둬야 와일문 반복에서 초기화 되지 않고 저장소를 하나만으로 유지한다
#메뉴로 숫자를 입력받아 처리하는 프로그램 작성
# 1. 숫자추가 2.숫자출력 3.합계 4.값으로 삭제 000 종료
while True :
    print("1. 숫자추가, 2.숫자출력, 3.합계, 4.값으로 삭제, 000 종료")
    num = int(input('숫자를 입력하시오'))
    if num == 1 :
        num = int(input('숫자를 입력하여 추가하시오'))
        numbers.append(num)
    elif num == 2 :
        print(numbers) # ,end = " " 하면 줄 유지 이후 탈출하고(들여쓰기 안하는 그래야 1번 실행됨 값 여러개면 여러번 실행될 수 있으니까) 프린트 하면 맨 처음 줄이 이탈없이 제대로 나온다
    elif num == 3 : 
        print(f'합계는 {sum(numbers)}입니다')    
    elif num == 4 :
        val = int(input('삭제하고자 하는 숫자를 입력하시오'))
        if val in numbers :
            numbers.remove(val)
        else: print('없음')
    elif num == 000 :
        break


    #올바른 코드 작성법(내가 쉽게)
    #우선 코드의 뼈대를 작성한다
    #예를 들면 위 코드에서 와일문 안에 이프문 작성하고 각각의 조건(넘 번호가 몇일때 출력할 문장까지)만 하고 기능은 하지않고 패스 이후 종료 브레이크문을 하고 이후에 기능 넣기
