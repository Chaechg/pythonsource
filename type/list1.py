# 리스트 자료형
# 자바의 배열, List와 같은 개념
# 인텍스로 접근, 삽입, 삭제 가능
# 인덱스의 값들은 특정 타입을 제한하지 않음


# 리스트 생성 - 대괄호 또는 리스트 함수
list1 = []
list2 = [1,2,3]
print(list1)
print(list2)

list1 = list()
list2 = list([1, 2, 3]) #함수를 써서 생성
print(list1)
print(list2)

list3 = ["a", "b", "c", 1, 2]
print(list3)

# 자바처럼 type이 제한되지 않는다.
list4 = ["a", "b", "c", 1, 2, 6.5, True]
print(list4)

list5 = ["a", "b", "c", ["Life", "is", "short"] ]
print(list5)

# 리스트를 다루는 방법

# 인덱싱과 슬라이싱
# 인덱싱
list3 = ["a", "b", "c", 1, 2]
print("list3[0]", list3[0])
print("list3[-1]", list3[-1])

list5 = ["a", "b", "c", ["Life", "is", "short"] ]
print("list5[2]",list5[2])
print("list5[3]",list5[3]) # ['Life', 'is', 'short']
print("list5[3][0]",list5[3][0]) # Life
print("list5[3][-1]",list5[3][-1]) # short

list6 = ["1", "2",["a", "b", ["Life", "is", "short"]]]
# is가 나오려면
print("list6[2][2][1]", list6[2][2][1])
print("list6[-1][-1][-2]", list6[-1][-1][-2])

# 슬라이싱
list3 = ["a", "b", "c", 1, 2]
print("list3[0:3]", list3[0:3])
print("list3[:3]", list3[:3])
print("list3[:-2]", list3[:-2])

list5 = ["a", "b", "c", ["Life", "is", "short"] ]
print("list5[3:]", list5[3:]) # [['Life', 'is', 'short']] 리스트 안의 리스트 형태로 나온다.
print("list5[3][:2]", list5[3][:2]) # ['Life', 'is']