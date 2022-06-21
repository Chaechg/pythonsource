# range() : 특정 범위를 지정하는 함수, 역순도 가능하다.

print(range(5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(5)))  # [1, 2, 3, 4]
print(list(range(0,10,2)))  # [0, 2, 4, 6, 8]


# 1 ~ 10 출력

for i in range(1,11):
    print(i, end=" ")

print()

# 1 ~ 100 짝수만 출력
i = 2
for i in range(2,101,2):
    print(i, end=" ")

print()
# 1~100 합계
sum1 = 0
for i in range(1,101):
    sum1 += i
print("1 ~ 100 합 : ", sum1)
print()

# # 사용자가 입력한 숫자까지 합계를 구한 후 출력하기
# num1 = int(input("숫자를 입력하세요 : ")) + 1 #num1의 숫자까지 포함하기 위해서
# hap = 0
# for i in range(0, num1):
#     hap += i
# print("총 합계는 ", hap)
# print()

# 1~100 합계 : range() + sum()
print("1~100 합계: ", sum(range(1,101)))
print("1~100 홀수 합계:", sum(range(1,101,2))) # 홀수의 합
print("1~100 짝수 합계:", sum(range(2,101,2))) # 짝수의 합

# 역순으로
for i in range(5, -1, -1):
    print(i, end=" ")


