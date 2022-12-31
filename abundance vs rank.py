import matplotlib.pyplot as plt
from math import log

# Read the number of each bird species from a file
with open('birds_counts.txt', 'r') as f:
    data = {}
    for line in f:
        species, count = line.split()
        data[species] = int(count)

# Calculate the Shannon index
n = sum(data.values())
shannon_index = 0
for count in data.values():
    p = count / n
    shannon_index -= p * log(p, 2)

# Plot the abundance rank graph
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
species, counts = zip(*sorted_data)
plt.plot([x+1 for x in range(len(counts))], counts, '-o')  # Shift the data points by 1 in the x-axis
plt.xlabel('Rank')
plt.ylabel('Number of Individuals')
plt.title('Abundance Rank Graph')

# Annotate each data point with the species name
for i, species in enumerate(species):
    plt.annotate(species, (i+1, counts[i]), xytext=(5,5), textcoords='offset points', rotation=45)

# Add the Shannon index to the graph
plt.text(len(species), max(counts), f'Shannon index: {shannon_index:.2f}', ha='right')

plt.show()
