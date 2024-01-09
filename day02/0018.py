#타입, 변수, 산술연산 (6개)
#조건문(if문)

a = 10

if a >5:
    print('5보다 큽니다')
    print('if가 참이면 동작')
print("if와 관계없다")

money = 1000
if money >= 4500:
    print("떡볶이를 먹습니다.")
    print("행복합니다.")
else:
    print("불행합니다.")

print("집에 왔어요")

#점수를 입력받아 70점 이상이면 합격, 아니면 불합격 기본적으로 출력이 끝나면 수고하셨습니다.

score = int(input("당신의 점수는?"))
if score >= 70:
    print("당신은 합격")
else:
    print("당신은 불합격")
print("수고하셨습니다.")
