# 원시타입, 내장함수 <-> import, pip
# 개발자는 값을 검증
# str타입
str1='10'
str2='3.14'
str3='홀짝홀짝홀짝홀짝'

#연산
print(str1 + str2)          # 연결 
print(str1 *10)             # 반복
print(str1[0])              # 문자열은 집합은 아니나 집합연산 사용 가능
print(str3[0:3])
str4= '8546457'
print(str4[0:3])
print(str4[0:])
print(str4[::2]) #시작부터 2의 간격으로 찍는다
str5='0123456789'
#홀수만 출력 1,3,5,7,9
#3의 배수 출력
print(str5[::2])
print(str5[::3])
#내장함수 len
print(len('15')) #문자의 길이를 재는 함수 또는 집합(리스트 등)을 잴 수 있다

#문자열은 변경 불가능 immutable <->mutable
#str5[3]='h'은 에러
str6= 'asdfg'
list6 = ['a','s','d',3,'g']
list6[3]='h'
print(list6) #리스트는 값 변경 가능
