# Users-Data-Analysis
**Project Overview**

This project involves extracting, cleaning, and analyzing user data from the DummyJSON Users API
. The goal is to explore demographic and physical attributes, such as age, height, weight, gender distribution, and city distribution, and visualize relationships between these attributes using Seaborn.

**Data Preparation**

Loaded data from the API and converted nested fields (e.g., address) into separate columns.

Checked for missing values and handled them.

Explored basic statistics: shape, data types, summary statistics, value counts for categorical columns.

**Analysis**

Calculated average age overall and by gender.

Counted number of users per gender.

Identified top 10 cities with the most users.

Calculated average height and weight.

Explored relationships between age and height/weight to detect trends or correlations.

**Visualizations**

Used Seaborn to create clear and informative visualizations:

Gender distribution

Age distribution

Height vs Weight scatter plot

Average age by gender

Top cities by user count

**Tools**

Python, Pandas, NumPy, Seaborn, Matplotlib, Requests, Jupyter Notebook
