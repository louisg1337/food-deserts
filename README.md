# Food Desert

People throughout America experience food insecurity in numerous ways, one of which being food deserts. These are regions in America where people have limited access to nutritious, affordable food. In these regions, fast food and convenience stores are typically the only food sources available, contributing to poor nutrition and long term health issues. 

The goal of this project is to identify those food deserts, and then recommend optimal locations for new food pantries based on the data given.

# Specific Goals

- Identify food deserts accross America.
- Predict the best locations for new food pantries, considering factors such as population need, accessibility, and budget constraints. 

# Data Collection
- To identify food deserts and predict optimal locations for new food pantries we need the following...
  - Grocery and food pantry locations, OpenStreetMap/Web Scraping
  - Census and socioeconomic information, US Census Bureau
  - Transportation accessibility data, GTFS

# Modeling Data Plan
- Identifying food deserts
  - A clustering technique can be applied to group areas based on certain factors, such as median household income, distance to closest food pantry/grocery store, population density, etc. We can then analyze these clusters to identify vulnerable areas that have low access to grocery stores, and are not economically well off. 
- Predicting optimal food pantry locations
  - These predicitons can be made using an optimization strategy through adding weights via a heuristic function. We can determine that heuristic function from different factors, such as food access, median income, population density, and transportation availability.
 
# Visualization
The food deserts will be visualized using a heatmap of America, showcasing areas that are lacking adequate food resources. The predictions for optimal food pantry locations will then be demonstrated on top of the map. There will be additional parameters you can play around with and tweak which can alter the locations of the optimal food pantries.

# Testing
I will train both the clustering and optimization algorithms on 80% of the data and evaluate their performance on the remaining 20%. This approach will help ensure that the models can generalize well and accurately identify patterns in unseen data. For further quality assurance, I will strategically remove food pantries from my dataset, and see if my prediction algorithm will suggest food pantries in those locations.
