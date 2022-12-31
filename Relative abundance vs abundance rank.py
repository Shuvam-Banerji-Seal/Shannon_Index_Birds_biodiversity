import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data from "birds_counts.txt"
species = []
counts = []
label = []
with open("birds_counts.txt", "r") as f:
    for line in f:
        items = line.split()
        species.append(items[0])
        counts.append(int(items[1]))

# Calculate the Shannon index
n = sum(counts)
p = [count/n for count in counts]
shannon_index = -sum([pi*np.log2(pi) for pi in p])

# Plot the relative abundance vs abundance rank graph
plots = plt.plot(range(1, len(species)+1), p, "o-", label=[f"{species[i]} ({counts[i]})" for i in range(len(species))])
plt.xlabel("Abundance rank")
plt.ylabel("Relative abundance")
plt.title("Birds' Biodiversity")
plt.xticks()


# Set the limits of the x axis to start from 1
#plt.xlim(1, len(species))


# Add the species names to the points in the plot at a distance from the graph lines
for i, txt in enumerate(species):
    plt.annotate(txt, (i+1, p[i]),rotation = 60, size = 8, xytext=(5, 2), textcoords="offset points",
                 ha="center", va="bottom")

# Print the Shannon index on the plot
plt.text(0.9, 0.9, f"Shannon index: {shannon_index:.3f}", transform=plt.gca().transAxes, ha="right", va="top")
# Create a txt file with species, abundance, ni/N and ln(ni/N) columns
with open("birds_biodiversity.txt", "w") as f:
    f.write("Species\tAbundance\tni/N\tln(ni/N)\n")
    for i in range(len(species)):
        f.write(f"{species[i]}\t{counts[i]}\t{p[i]:.3f}\t{np.log(p[i]):.3f}\n")




plt.show()
