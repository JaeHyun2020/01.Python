# uTube 이수안 컴퓨터연구소의 파이썬 프로그래밍 6장 입력과 출력 참조

# 표준 입출력 함수 : input(), print()
# name = input("이름:")
# print(name) 

# 섭씨 온도를 화씨온도로 변환. f = (c * 1.8) + 32 
# c = float(input("섭씨온도: "))
# f = (c * 1.8) + 32
# print("화씨온도: ", f)

# 구구단 출력 
i = int(input("출력할 단:"))
for j in range(1,10):
    print("{0} x {1} = {2}".format(i, j, i * j))
    
# 8분부터 
    