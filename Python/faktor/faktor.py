import math

line = input()
published_articles, impact_factor = line.split()
published_articles = int(published_articles)
impact_factor = str(int(impact_factor) - 1)
impact_factor = float(impact_factor + ".0001")

print(math.ceil(published_articles * impact_factor))
