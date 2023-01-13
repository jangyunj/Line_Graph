import matplotlib.pyplot as plt

x1 = [2012, 2013, 2014, 2015, 2016, 2017]
y1 = [15000, 18000, 16000, 19000, 22000, 24000]

plt.plot(x1, y1, color='orange', linestyle='solid', linewidth=3, marker='o', markerfacecolor='orange', markersize=10, label='Annual Sales 2012-2017')


x2 = [2012, 2013, 2014, 2015, 2016, 2017]
y2 = [18000, 18000, 18000, 18000, 18000, 18000]

plt.plot(x2, y2, color='blue', linestyle='dotted', linewidth=5, label='Yearly quota')

plt.legend()

for a, b in zip(x1, y1):
    plt.text(a, b, str(b))

plt.grid(axis='y', color='#ccc', linestyle='-', linewidth=2.5)

plt.xlabel('Years')
plt.ylabel('Sales(USD)')
plt.title('Annual Sales Trend')
plt.show()