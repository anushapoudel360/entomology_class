import matplotlib.pyplot as plt

# defining the species in an array
insect_species = [
    "Dysdercus_cingulatus",
    "Apis_mellifera",
    "Apis_cerana",
    "Xylocopa_virginica",
    "Spialia_galba",
    "Danaus_plexippus",
    "Vespula_vulgaris",
    "Campsomeriella_collaris",
    "Coccinella_septempunctata"
]

# the number of individuals in the distribution for each corresponding species
number_of_individuals = [6, 56, 27, 20, 6, 10, 8, 5, 3]

# the bar chart
plt.figure(figsize=(8, 4))

# x-coordinates of the bars is insect species.
# y-coorinates is the heights of the bars which is number of individuals.
plt.bar(insect_species, number_of_individuals, color='green')

plt.xlabel("Insect Species") # Label for x-axis
plt.ylabel("Number of Individuals (n)") # Label for y-axis
plt.title("Distribution of Insect Species by Count") # Main title of the plot

plt.xticks(rotation=45, ha='right')

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()
