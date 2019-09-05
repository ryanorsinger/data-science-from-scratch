# We visualize data for two primary reasons:
# 1 - to explore data
# 2 - to communicate data

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

# Title the chart
plt.title("Nominal GDP")

# Label the axes
plt.ylabel("Billionso f $")
plt.show()

# Bar Charts
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

# Label x-axis
plt.xticks(range(len(movies)), movies)
plt.show()


## Another Bar Chart
from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
    histogram.values(),
    edgecolor=(0, 0, 0))

plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# Of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()  



# Example of a misleading chart
mentions = [500, 505]
years = [2017, 2018]
plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

plt.ticklabel_format(useOffset=False)

# make the misleading axix
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("look at the 'Huge Increase'")
plt.show()

# Back to normal
plt.axis([2016.5, 2018.5, 0, 550])
plt.title("Not So Huge Anymore")
plt.show()

