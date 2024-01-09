#숫자 리스트 - 추가, 합계, 목록, 변경, 삭제 를 함수버젼으로

'''

numbers=[]
while True:
    print_menu()
    select = input_select()
    if select == '1' :
        add_value()
    elif select =='2':
        list_numbers()
    elif select =='3':
        update_number()
    elif select =='4':
        delete_number()
    elif select =='999':
        fin()
시작 전 모습
'''


numbers=[1,2,3,4,5]
def print_menu():
    print('####숫자CRUD####')
    print('1:추가, 2:목록, 3:삭제, 999:종료')
def input_select():
    return input('메뉴 선택 : ')    #셀렉트가 받아가므로 리턴해줌

def add_value():
    value = int(input('값입력:'))
    numbers.append(value)
def list_numbers():
    for num in numbers:
        print(num, end=" ") # 줄을 안바꾸게 하는게 end파라미터 #줄 바꾸지 말고 공백으로 만들어라
    print() #마지막에 줄 바꾸게 함
def delete_number():
    value = int(input('삭제할 값 입력'))
    index = 0
    for num in numbers:
        if num == value:
            del numbers[index]
        index= index+1
while True:
    print_menu()
    select = input_select()
    if select == '1' :
        add_value()
    elif select =='2':
        list_numbers()
    elif select =='3':
        delete_number()
    elif select =='4':
        delete_number()
    elif select =='999':
        break
