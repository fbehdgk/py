# collection 타입 : list, tuple, set,dictionary
    # sequence 타입 : list, tuple

#list와 tuple 의 차이점
 #list는 mutable(가변언어), tuple은 immutable(값 못바꿈 그리고 이거엔 str도 포함임 불변)
list1 = [1,3,5]
tuple1 = tuple(list1)
list1 = list(tuple1)

#데이터가 있다 -> CRUD(크리에이트(리스트에 값추가) 리드 업데이트 딜리트)
list1.append(100)
print(list1)
#for 변수 in 컬렉션 :
x = [1,2,3,4]
print(x)
print('******')
i = 0
for x[i] in list1 :
    i=+1
    print(x)
print('**********')

print(x)
#index (리스트에서 값 위치로) 업데이트
list1[1] = 200
print(list1)
#delete
print('---------')
list1.remove(200) # 알아서 찾아서 지움
print(list1)
del list1[2] #내가 찾아서 지정해서 지움
print(list1)
print('/////////')
list1 = [1,2,3,4]
x = [0,0,0,0]
i = 0
for x[i] in list1 :
    i=i+1
print(x)