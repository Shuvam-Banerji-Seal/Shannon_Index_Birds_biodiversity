# Biodiversity Analysis with Python

This repository contains two Python scripts for analyzing biodiversity based on bird species abundance data stored in the "birds_counts.txt" file. The scripts calculate the Shannon index and generate visualizations to illustrate the abundance rank and relative abundance of bird species.

## Abundance Rank Graph

### Algorithm Overview

1. **Read Data:**
   - Read the number of each bird species from the "birds_counts.txt" file.

2. **Calculate Shannon Index:**
   - Calculate the Shannon index based on the species counts.

3. **Plot Abundance Rank Graph:**
   - Sort the data by counts in descending order.
   - Plot the abundance rank graph, shifting data points by 1 on the x-axis.
   - Annotate each data point with the species name.
   - Add the Shannon index to the graph.

## Biodiversity Analysis

### Algorithm Overview

1. **Read Data:**
   - Read species names and counts from the "birds_counts.txt" file.

2. **Calculate Shannon Index:**
   - Calculate the Shannon index based on the species counts.

3. **Plot Relative Abundance vs Abundance Rank Graph:**
   - Plot the relative abundance vs abundance rank graph.
   - Annotate each point with the species name.
   - Print the Shannon index on the plot.

4. **Create TXT File with Additional Data:**
   - Create a text file ("birds_biodiversity.txt") with species, abundance, ni/N, and ln(ni/N) columns.


## Conclusion

Both scripts provide insights into the biodiversity of bird species based on their abundance. The abundance rank graph visually represents the abundance of each species, while the relative abundance graph highlights the distribution of species based on their ranks. The calculated Shannon index quantifies the biodiversity in each analysis.

## How to Use

1. Ensure you have `matplotlib`, `numpy`, and `pandas` installed:

   ```bash
   pip install matplotlib numpy pandas
   ```

2. Run each script:

   ```bash
   python abundance_rank_graph.py
   python biodiversity_analysis.py
   ```

The resulting plots will be displayed, and additional data will be stored in the "birds_biodiversity.txt" file for further analysis.
