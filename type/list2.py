# 리스트 연산자

# + : 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a[0] + b[1])  # 1 + 5 = 6

# * : 반복 또는 요소들의 곱
a = [1, 2, 3]
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(a[1] * a[2])  # 6

# 리스트 수정
a = [1, 2, 3]
a[2] = 4
print(a)  # [1, 2, 4]
a[1] = "Life"
print(a)  # [1, 'Life', 4]

b = [4, 5, 6]
b[1:2] = [10, 11]
print(b)  # [4, 10, 11, 6] 1번 요소자리에 10, 11을 줌
c = [4, 5, 6]
c[1] = [10, 11]
print(c)  # [4, [10, 11], 6]
# 특정 요소를 지정하는 것과 연속된 범위를 지정하는 것의 결과의 차이가 있다.

# 리스트 삭제
a = [1, 2, 3]
a[1:3] = []
print(a)  # [1]

a = [1, 2, 3]
del a[1]  # 리스트 요소 삭제
print(a)  # [1, 3]
del a  # del 객체 삭제(다른 자료형들도 삭제 가능)

# 문제
# 리스트 안의 숫자가 100 이상인 숫자 출력하기
print("*" * 50)
print("100 이상 숫자")
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for i in numbers:
    if i >= 100:
        print(i)
print("*" * 50)
print("홀/짝 판별")
# 리스트 안의 숫자가 홀수인지 짝수인지 출력하기
for i in numbers:
    if i % 2 == 1:
        print("{} 홀수".format(i))
    elif i % 2 == 0:
        print("{} 짝수".format(i))
print("*" * 50)
# 리스트 안의 숫자들의 자리수 출력하기
print("각 숫자의 자릿수 출력")
for i in numbers:
    print("{} : {} 자릿수".format(i, len(str(i))))
print("*" * 50)

# 아래 리스트를 풀어서 출력
list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

# 출력결과 1 2 3 4 5 6 7 8 9 로 나오기를 원한다.
for list1 in list_of_list:
    for num in list1:
        print(num, end=" ")

# 리스트 함수
# 1) append() : 마지막 요소로 추가
list1 = [1, 2, 3]
print(list1)

# 하나의 요소 추가
list1.append(7)
print(list1)

# 여러 개의 요소 추가
list2 = [4, 5, 6]
print(list1 + list2)
list1.append(list2)
print(list1)  # [1, 2, 3, 7, [4, 5, 6]] 리스트 안의 리스트로 들어온다.

# 1~100 숫자 중에서 짝수만 들어있는 리스트 생성하고 출력하기
even = []  # even = list()
for i in range(2, 101, 2):
    even.append(i)
print(even, end=" ")

print()
print("*" * 50)

# 2) sort() : 오름차순 정렬
list1 = [25, 75, 15, 9, 6, 3, 35]
print("정렬 전", list1)
list1.sort()
print("정렬 후", list1)

print()
list2 = ["k", "z", "b", "a", "q", "r"]
print("정렬 전", list2)
list2.sort()
print("정렬 후", list2)  # 알파벳 순서대로

print()
list3 = ["k", "z", "B", "a", "Q", "r"]
print("정렬 전", list3)
list3.sort()
print("정렬 후", list3)  # 대문자 먼저 아스키코드 A-65, a-97

print()
list4 = ["ㅎ", "ㅋ", "ㄱ", "ㄷ", "ㅈ", "ㄹ"]
print("정렬 전", list4)
list4.sort()
print("정렬 후", list4)  # ['ㄱ', 'ㄷ', 'ㄹ', 'ㅈ', 'ㅋ', 'ㅎ']

print()
list5 = ["abc", "tail", "bcd", "test", "animal", "korea"]
print("정렬 전", list5)
list5.sort()
print("정렬 후", list5)

print()
# sort(reverse=True) : 내림차순 정렬
list1 = [25, 75, 15, 9, 6, 3, 35]
print("정렬 전", list1)
list1.sort(reverse=True)
print("정렬 후", list1)

print()
# 3) reverse() : 리스트 역순으로 처리
print("reverse() 사용")
list1 = [25, 75, 15, 9, 6, 3, 35]
print("정렬 전", list1)
list1.sort()
list1.reverse()
print("정렬 후 거꾸로 출력", list1)

# 4) index() : 위치반환
list1 = [34, 25, 9, 75]
print("9가 있는가? ", list1.index(9))
# print("45가 있는가? ", list1.index(45)) # ValueError: 45 is not in list

# 5) insert() : 리스트 내의 특정 위치에 요소 삽입
list1 = [34, 25, 9, 75]
list1.insert(1, 56)  # 1번 자리에 56 요소를 추가
print(list1)

# 6) remove() : 리스트 요소 제거
list1 = [34, 25, 9, 75, 9]
list1.remove(25)
print(list1)  # [34, 9, 75, 9]
list1.remove(9)  # 중복된 경우 앞 요소 제거
print(list1)  # [34, 75, 9]

# 7) pop() : 리스트 맨 마지막 요소 돌려주고 요소는 삭제
list1 = [34, 25, 9, 75, 9]
list1.pop()
print(list1)  # [34, 25, 9, 75]

# pop(인덱스 값) : 해당 인덱스 요소 돌려주고 그 요소는 삭제
print(list1.pop(1))  # 25
print(list1)  # [34, 9, 75]

# 8) count() : 리스트 안의 특정 요소의 개수 세기
list1 = [34, 25, 9, 75, 9]
print(list1.count(9))  # 2 : 9가 몇개 들어있는지 물어봄

# 9) extend() : 리스트 확장(+와 같은 결과)
list1 = [34, 25, 9, 75, 9]
list2 = [11, 12, 13]
list1.extend(list2)
print(list1)  # [34, 25, 9, 75, 9, 11, 12, 13]

# 10) clear() : 리스트 요소 모두 삭제
list1.clear()
print(list1)  # []

# 리스트 안의 요소가 비어 있는 경우는 false로 인식
list1 = []
if list1:
    print("True")
else:
    print("False")
# 리스트 구조에서 아무 요소가 없다면 false로 인식된다.

str1 = ""
if str1:
    print("True")
else:
    print("False")
# 문자열도 비어있다면 false로 인식한다.

# 요소 in 리스트 : 해당 요소가 리스트 안에 들어있는지 판별
# 굳이 for문 같은 loop를 돌릴 필요 없다.
fruit = ["사과", "배", "딸기", "수박", "메론"]

if "딸기" in fruit:  # not in 개념도 가능하다.
    print("딸기 있음")
else:
    print("딸기 없음")

# enumerate() : 인덱스 값 사용
list1 = [23, 12, 35, 53, 19]
for item in list1:
    print(item)

print()

list1 = [23, 12, 35, 53, 19]
for item in enumerate(list1):
    print(item)

print()
# 인덱스 값을 변수로 사용이 가능하다.
list1 = [23, 12, 35, 53, 19]
for idx, item in enumerate(list1, start=1):
    print("%d : %d" % (idx, item))
