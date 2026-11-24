# print("안녕")

# name = "홍길동"  # str 문자열
# age = 17  # int 정수형
# height = 172.5  # float 실수형
# is_student = True  # 참/거지, boolean형


# def add(a, b, giho):
#     return


# print(add(1, 2, "*"))

# for i in range(5, 0, -1):
#     print("*" * i)

height = 5

for i in range(height):
    stars = i + 1
    spaces = height - stars
    print(" " * spaces + "*" * stars)
