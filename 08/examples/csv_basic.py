import csv
import matplotlib.pyplot as plt
lists = []
header = []
with open('slides/08/examples/example.csv', 'r') as f:
    reader = csv.reader(f)
    header = reader.__next__()[0].split(';')
    lists = [[] for _ in range(len(header))]
    for row in reader:
        for i, item in enumerate(row[0].split(';')):
            lists[i].append(int(item))
plt.plot(lists[0], lists[1])
plt.show()
