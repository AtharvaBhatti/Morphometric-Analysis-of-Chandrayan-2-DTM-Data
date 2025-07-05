Morphometric Analysis of Lunar Craters using Chandrayaan-2 DTM Data

THE PDF FILE AND LOOM VIDEO EXPLAINS OUR WORK AS WELL.

This project performs morphometric analysis of lunar craters using high-resolution Digital Terrain Model (DTM) data from the Chandrayaan-2 mission. The goal is to extract and analyze crater depth-to-diameter (d/D) relationships both individually and across multiple craters.

📁 File Overview
1. CV_Project.ipynb
This is the main Jupyter Notebook that serves as a pipeline for:

Loading crater DTM and orthoimage data (GeoTIFF format)
Extracting elevation profiles of craters
Identifying crater rims and bottoms
Calculating key metrics: diameter (D), depth (d), and depth-to-diameter ratio (d/D)
Visualizing crater profiles and spatial distribution
Generating datasets for further regression and statistical analysis
It combines and visualizes the logic of the individual and combined Python scripts below in a more interactive and iterative form.

2. dbyD_individual.py
This script performs analysis on a single crater:

Loads a specific DTM raster
Extracts a horizontal elevation profile through the center
Smooths the profile and identifies rim and bottom points
Computes the crater’s diameter (D), depth (d), and d/D ratio
Plots the profile for visual validation
👀 Great for checking the quality of individual crater profiles.

3. dbyD_combined.py
This script processes multiple craters from a precomputed CSV file:

Loads a CSV file containing diameters and depths for many craters
Performs a linear regression between depth and diameter
Plots the regression line and scatter of points
Displays the regression equation and R² value
📊 Useful for understanding overall morphometric trends across a crater dataset.

🛠️ Dependencies
All scripts and notebooks require the following Python packages:

numpy
pandas
matplotlib
rasterio
scipy
scikit-learn
Install them using:

pip install numpy pandas matplotlib rasterio scipy scikit-learn
🚀 How to Run
To explore or modify crater analysis visually, open CV_Project.ipynb in Jupyter Notebook or JupyterLab.
Use dbyD_individual.py to analyze and validate the depth and diameter of a single crater.
Use dbyD_combined.py for bulk regression analysis on multiple craters using preprocessed metrics.
