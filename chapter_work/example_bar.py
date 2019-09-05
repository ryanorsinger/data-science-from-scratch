from matplotlib import pyplot as plt

## Another Bar Chart
from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

x = [x + 5 for x in histogram.keys()]
y = histogram.values()

print(x)
print(list(y))
plt.bar(y, x, color = (0.2, 0.4, 0.6, 0.6))

plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# Of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()  



