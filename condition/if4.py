# 다중 조건
# if ~ elif ~ else

num = 90
if num >=90:
    print("등급A")
elif num >= 80:
    print("등급B")
elif num >= 70:
    print("등급C")
else:
    print("등급D")

# 점수 구간에 맞춰 학점 출력하기
# 점수 입력 받은 후 학점 출력
# A : 81~100
# B : 61~80
# C : 41~60
# D : 21~40
# F : 나머지

score = 88
if score > 80:
    print("A")
elif score > 60:
    print("B")
elif score > 40:
    print("C")
elif score > 20:
    print("D")
else:
    print("F")

# 산술 계산기 => 두 개의 숫자 입력 받기
# +,-,*,/,//,**,%

num1 = int(input("첫번째 수 입력"))
op = input("+,-,*,/,//,**,% 중 연산자 입력")
num2 = int(input("두번째 수 입력"))

if op == "+":
    print(num1, op, num2, "=", num1+num2)
elif op == "-":
    print(num1, op, num2, "=", num1-num2)
elif op == "*":
    print(num1, op, num2, "=", num1*num2)
elif op == "/":
    print(num1, op, num2, "=", num1/num2)
elif op == "//":
    print(num1, op, num2, "=", num1//num2)
elif op == "**":
    print(num1, op, num2, "=", num1**num2)
elif op == "%":
    print(num1, op, num2, "=", num1%num2)
else:
    print("잘못 입력하셨습니다.")