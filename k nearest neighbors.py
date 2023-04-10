import math

bread_sales_data = {(5, 1, 0): 300, (3, 1, 1): 225, (1, 1, 0): 75, (4, 0, 1): 200, (4, 0, 0): 150, (2, 0, 0): 50}
new_data = (4, 1, 0)
k = 4

distances = []
for key in bread_sales_data.keys():
    n = 0
    for i in range(3):
        n += (key[i] - new_data[i]) ** 2
    distances.append(str(n) + " " + str(bread_sales_data[key]))
mindist = []
for dist in distances:
    d, v = map(int, dist.split())
    mindist.append(d)
mindist.sort()
mindist = mindist[:k]
s = 0
count = 0
for dist in distances:
    d, v = map(int, dist.split())
    print(d, v)
    if d in mindist and count < k:
        s += v
        count += 1
print(s / k)
