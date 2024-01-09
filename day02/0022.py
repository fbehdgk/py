#섭씨를 입력받아 화씨로 출력
#degrees_Celsius = int(input("섭씨 : "))
#degrees_Fahrenheit = (degrees_Celsius * 1.8) + 32 #변환공식
#print(f"섭씨 {degrees_Celsius}도는 화씨 {degrees_Fahrenheit}도")

# 온도와 종류를 입력받으시오
# 예) 온도: 35
# 예) 종류: 섭씨
#종류가 섭씨면 온도를 화씨로 그리고 반대도 적용되게

degrees = int(input("온도 입력 : "))
kind = input("종류 입력 [화씨, 섭씨 선택]: ")
if kind == "섭씨":
    result = (degrees *1.8) + 32
    print(f"섭씨 {degrees}는 화씨 {result}입니다.")
elif kind == "화씨":
    result = (degrees -32) / 1.8
    print(f"화씨 {degrees}는 섭씨 {result}입니다.")
else:
    print("섭씨, 혹은 화씨로 써주세요.")

#1.섭씨면 화씨로, 화씨면 섭씨로 변경
#2.온도 받기 -> 입력온도가 섭씨? 화씨?
#3.종류 받기 -> kind
#4. kind가 섭씨면 화씨로 변환.
#5. kind가 화씨면 섭씨로 변환.
    

