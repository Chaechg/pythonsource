# 현재 시간이 오전인지 오후인지 출력하기
# 현재시간 불러오기 - 클래스 사용
import datetime

now = datetime.datetime.now()
print(now) # 2022-06-07 18:55:32.152225
print("{}년 {}월 {}일 {}시 {}분 {}초".
      format(now.year,now.month,now.day,now.hour,now.minute,now.second))
      # 2022년 6월 7일 18시 58분 5초

# 오전, 오후
if now.hour < 12:
    print("오전")
else:
    print("오후")

# 삼항 연산자
# 자바 : 조건 ? 참 : 거짓
# 파이썬 : 참일때 실행하는 구문 if 조건 else 거짓일 때

str = "안녕하세요" if True else "반갑습니다."
print(str)

# [] : 리스트 - 비어있는 경우 false로 인식
a = []
str = a if a else "비어있는 배열"
print(str)

# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")
