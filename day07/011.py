# 추가 목록 삭제 종료

numbers = [1,2,3,4,5]

def print_menu():
    print('##1.추가 2.목록 3.삭제 999.종료##')
def add_value():
    value = int(input('값입력:'))
    numbers.append(value)
def list_numbers():
    for num in numbers:
        print(num)
def delete_number():
    value = int(input('삭제할 숫자 입력'))
    index = 0
    for num in numbers:
        if value == num:
            del numbers[index]
        index+1
while True :
    print_menu()
    select = int(input('메뉴입력'))
    if select == 1:
        add_value()
    elif select == 2:
        list_numbers()
    elif select == 3:
        delete_number()
    elif select == 999:
        break