#f문자열
#replace : 치환
str4 = '010-1111-2222'
print(len(str4))
#print,len처럼 소속없이 단독으로 사용가능한걸 함수 + 소속있는 메소드도 포함임
str4.replace("-",".") #메소드 접속. 그러나 문자열은 변경 불가능해서 안바뀜
#replace처럼 .을 통해 사용하는것은 메소드라고한다 타입은 함수도 가질 수 있다 
str4 = str4.replace("-",".") # 문자열을 바꾼것이 아니고 대상(함수)를 바꾼것
print(str4)

str4 = str4.replace("1111","xxxx")
print(str4)

#"000000-2*******"
j1 = "3451324-20000000"
j1 = j1.replace(j1[9:],"*******") # 리플레이스로 9번자리문자부터 *로 출력
print(j1)


str5= "         aa aa           " #가운데 공백은 내용으로 취급하여 지우지 않는다
print(str5.split())#공백제거
