a = 55
if a < 100:
    print("a는 100보다 작은 수이다.")
else:
    print("a는 100보다 큰 수이다.")

score, grade = 90, "A"
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")
    
# 사용자에게 숫자 입력받고, 숫자가 짝수, 홀수인지 출력하기
num = int(input("숫자를 입력해 주세요 : "))
if num % 2 == 0:
    print("해당 숫자는 짝수입니다.")
else:
    print("해당 숫자는 홀수입니다.")


