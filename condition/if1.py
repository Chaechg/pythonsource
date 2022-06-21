# {}를 사용하지 않음 / 들여쓰기로 같은 실행 블럭을 나타냄
# :을 써서 조건문을 맺음

a = 200
if a < 100:
    print("a는 100보다 작다")

# a는 100보다 크고 200과 같거나 작다
if 100 < a <= 200:  #a > 100 and a <= 200
    print("a는 100보다 크고 200과 같거나 작다")

a, b, c = 12, 6, 18

# 세 수 중에서 가장 큰 수 출력
        # if a - b > 0 and a - c > 0:
        #     print(a)
        # elif b - a > 0 and b - c > 0 :
        #     print(b)
        # else:
        #     print(c)
max = a
if max < b:
    max = b
if max < c:
    max = c

print("가장 큰 수 : ",max)
print("가장 큰 수 : %d" % max)
print("가장 큰 수 : {}".format(max))