# ELSCORE.py
#
# Texas Instrument TI-84 Plus CE-T Python Edition
#
# X,Y for aa bestemme skuddverdi
# morten.teinum@gmail.com
# 2020-10-30: Rev 1

import math

programs = [
	"10m luft rifle",
	"10m luft pistol 50m rifle",
	"25m og 50m presisjon",
	"25m grov presisjon",
	"300m rifle",
	"25m fin duell (min 5)",
	"25m grov duell (min 5)",
]

for i in range(len(programs)):
  print("{}: {}".format(i, programs[i]))

# what to do
p=int(input("Program: "))
x=float(input("X: "))
y=float(input("Y: "))

# calulate radius
r = math.sqrt(x * x + y * y)

print("radius", round(r, 3))

# 9,9 -> 0
# 10,9 -> 10,0
score_table   = [ 0.25, 0.80, 2.78, 2.9825, 5.4, 5.28, 5.4825 ]
score_table_x = [ 0.25, 0.80, 2.50, 2.5000, 5.0, 4.00, 4.0000 ]

index = 0
current_r = score_table[p]

while r > current_r:
  current_r += score_table[p] if index < 9 else score_table_x[p]
  index += 1

# print answers
print("index", index)
print("current_r", round(current_r, 3))
print("skuddverdi", round(10.9 - index / 10, 1))
print("")