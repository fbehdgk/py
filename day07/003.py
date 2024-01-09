#할일관리 while문을 이용해서 답을 저장가능
tno = 1
todos = [
    {'tno':tno,'title':'할일1','reg_day':'2022-01-09','finish':False},
    {'tno':3,'title':'할일3','reg_day':'2022-01-09','finish':False}
]
tno = 2
#전체읽기
for todo in todos:
    print(todo)
# 할일번호를 입력받아 할일을 찾아 출력
찾았니 = False
do_num = int(input('할일번호'))
for todo in todos:
    if todo['tno'] == do_num:
        print(todo['title'])
        찾았니= True
        break 
if 찾았니 == False:
    print('할일이 없다')
    