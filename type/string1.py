# 문자열 자료형
# '', "", """ """, ''' '''
str1 = "Hello World"
str2 = 'Hello World'

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
str3 = "Life is too short\nYou need Python"
str4 = """
        Hello World
        Life is too short
        You need Python
"""

str5 = "Hello's"

print(str4)
print(str5)

# 문자열 응용
# + : 결합
print("Python" + " is fun")

# * : 복제
print("Python"*2)
print("*"*50)
print("My Program")
print("*"*50)

# 문자열 인덱싱과 슬라이싱
# 인덱싱 : 0부터 시작, -이면 뒤에서 인덱싱
str1 = "Life is too short"
print(str1[3]) #인텍싱 : 0부터 인덱싱을 시작, -값은 뒤에서부터 시작

print(str1[0:4]) # Life 뒤의 숫자는 포함하지 않는다.
print(str1[4:8])
print(str1[9:]) # 생략은 맨 처음 또는 맨 뒤를 의미한다.
print(str1[:17])
print(str1[0:-4])

str1 = "대한민국"
for s in str1:
    print(s, end="")

print()

# 문자열 길이
print("문자열 길이 : ", len(str1))


