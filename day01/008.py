#함수, 변수 -> 이름을 가진다 -> 재사용을 위함
#a = 80
#jumsu = 85 이쪽이 이해하기쉽다.

#성적합계 220

#작명법은 가독성있게 작성해야한다
#sum_of_all_scores = 220 파이썬식 작성법 , 소문자, 언더바
#sumOfALLScores = 220 자바식 작성법 , 중간대문자
#SumOfAllScores = 220 C언어식 작성법 , 앞자 대문자

#키워드(예악어)는 사용할 수 없다.
#파이썬이 사용하는 단어는 사용불가 -> True같은 이름은 불가

#your_name = "김영진"
your_name = '김영진'
nai = 22
#제 이름은 김기준
print("제 이름은 " + your_name)
print("제 이름은", your_name)
#나이를 1증가시킨 후 나이는 23이라고 출력
nai += 1
print("나이는", nai , "살")

our_animal_name = "초코"
our_animal_syurui = "강아지"
syumi = "산책"
ski = "좋아해요"

print("우리집",our_animal_syurui,"이름은", our_animal_name+"입니다.")
print(our_animal_name + "는(은)", syumi + "을(를)",ski)

#3000000의 변수만들고 출력
salary = 3000000
print("급여 : " + str(salary))

samsung_electronics_stock_price = 79000# 가격은 api로 받아온다고 생각해야함
고객의주가총액 = samsung_electronics_stock_price*10
print("총 평가금액 : " + str(고객의주가총액)+"원")


