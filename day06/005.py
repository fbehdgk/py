#bool
b1,b2,b3,b4 = True,True,True,False
print((b1 and b2)or (b4 and b2))

nai = 30
gender='여자'
city = '인천'
#나이가 20이상이고 성별은 여자
gender == '여자'and   nai >=20
#나이가 20이상이고 성별은 여자인 사람
# (또는) 인천에 사는 사람
#둘중 하나 만족 의 식으로 줄을 바꾸면 또는을 의미한다 컴활 1급시험 엑셀 시트에서 찾으시오
(gender == '여자'and   nai >=20)or city =='인천'

