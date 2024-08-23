# ax + by = c
# dx + ey = f 방정식 풀기
# a, b, c, d, e, f 정수로만 주어짐 범위 [-1000, 1000]

a, b, c, d, e, f = list(map(int, input().split(' ')))

# 첫번째 방정식에 d 곱하고 두번째 방정식에 a 곱하고 빼기
#  d * (ax+by = c)
#- a * (dx+ey = f)
#------------------
# (db-ae)y = c-f
# y = cf / (db-ae)

y = (d*c-a*f) / (d*b-a*e)

# y 대입
# ax = c - by
# x = (c-by) / a
if a!=0:
    x = (c - b*y) / a
else:
    x = (f - e*y) / d

print(int(x), int(y))







