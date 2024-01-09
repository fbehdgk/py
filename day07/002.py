todos = [
        {'tno':1,'title':'자바공부','finish':False},
        {'tno':5,'title':'파이썬공부','finish':False}
        # 중간에 삭제 등의 이유로 빈번호가 생겨도 모든 tno를 바꾸어 채우지 않고 빈 번호로 놔둔다(비용문제)
         ]

#Create 할일 정보 받아와서 만들기
'''tno = 4
title = input('할일 입력 : ')
todo = {'tno':tno,'title':title,'finish':False}              
todos.append(todo)
tno = tno + 1'''
#Read : for 로 todos 출력
for todo in todos:
    print(todo)
#Update : tno로 찾아서 finish를 토글 못찾을시 아무것도 안한다
input_tno = int(input('변경할 할일번호 :'))
for todo in todos :
    if todo['tno'] == input_tno:
        todo['finish'] = not todo['finish']
        break

input_title = input('변경할 일정 :')
input_title2 = input('변경되는 일정 :')
for todo in todos :
    if todo['title'] == input_title:
        todo['title'] = input_title2
        break    
print(todos)

#Delete : 우선 원하는 번호를 입력해서 그 번호를 목록에서 찾고 번호에 있는 리스트를 지운다
del_tno = int(input('삭제할 할일번호 :'))
for todo in todos :
    if todo['tno'] == del_tno:
        todos.remove(todo)
        break
print(todos)
