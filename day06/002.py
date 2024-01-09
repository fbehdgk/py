#int 숫자타입 -> 타입마다 사용가능한 연산또는 함수가 다르다
#산술연산 : + - * / // % 
num1, num2 = 10, 3.14
# + - * / 결과출력 한줄로
print(f'합계 : {num1 + num2},차 :{num1 - num2},곱 :{num1 * num2},나누기 :{num1 / num2}')
num2 = 5
print(f'몫 : {num1//num2} 나머지 : {num1%num2}')
print(-num1)
#함수는 이름을 가진 기능 -> 재사용,내장함수(import없이 사용 가능)
#abs는 절대값 계산
print(abs(-100))
print(abs(100))
