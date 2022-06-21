# %d : 숫자, %f : 실수, %s : 문자열, %c : 문자, %% : % 표현

print("%d" % 100)   # 100
print("%5d" % 100)  #   100 (앞에 공백)
print("%05d" % 100) # 00100 (공백을 0으로 채움)
print()
print("%5s" % "hi") #    hi(앞 세자리 공백)
print("%s" % "hi")  # hi
print()
print("%-8.2f" %123.21)     # 123.21(전체 8자리, 소수점은 2 자리, -은 왼쪽정렬)
print("%8.2f" %12.21)       #    12.21(오른쪽 졍렬)
print("%8.2f" %12.2134567)  #    12.21
print()
print("I eat %d apples" % 3)
print("I eat %d apples" % 3)
print("I eat %d apples" % 3)
print()
print('%d : %s' % (1, "홍길동"))