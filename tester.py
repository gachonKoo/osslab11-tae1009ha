import geo.utils as utils

# calculate the length of hypotenuse (c) when a=3 and b=4
a, b = 3, 4
c = utils.pythagoras(a, b)  # 함수 이름 pythagoras로 수정
print('c =', c)

# calculate the area of circle with radius r = 10
r = 10
area = utils.circle(r)  # 함수 이름 circle로 수정
print('area =', area)