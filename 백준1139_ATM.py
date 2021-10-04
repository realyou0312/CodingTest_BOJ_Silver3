# 백준 1139번 ATM
# https://www.acmicpc.net/problem/11399


N = int(input())

time = list(map(int, input().split()))
time.sort() # 시간 오름차순 정렬

total = 0
temp = 0

for i in time:
    temp += i # 걸린시간을 누적
    total += temp # 다음 사람의 순서 시간을 반영

print(total)