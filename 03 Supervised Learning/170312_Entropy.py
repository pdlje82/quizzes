import math

p1 = 1/3.
p2 = 2/3.

entropy = - p1 * math.log(p1, 2) - p2 * math.log(p2, 2)
print entropy

information_gain = 1 - 3/4. * entropy

print information_gain