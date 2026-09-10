# Newcastle GP Accessibility Dashboard

*Live app:* [newcastle-gp-dashboard.streamlit.app](https://newcastlegpdashboard-hrw7vvyvfqvulpuzicwups.streamlit.app/)

## Overview
An interactive dashboard exploring GP surgery accessibility across Newcastle upon
Tyne's 26 electoral wards. Built as a deployed extension of my earlier geospatial
accessibility analysis, turning a static notebook output into a live, explorable
tool.

## Features
- Headline KPI metrics: total wards, total GP surgeries, wards with zero GP access
- Ward-level dropdown explorer showing population, GP count, and GPs per 10,000
  residents for any selected ward
- Live choropleth map that highlights the selected ward against the full
  accessibility pattern across Newcastle

## Method
Builds on the analysis from my [Newcastle GP Accessibility capstone](https://github.com/jims01/Healthcare-Accessibility) —
GP locations from OpenStreetMap (osmnx), ward boundaries and Census 2021
population from ONS, with a 1km buffer analysis producing a GPs-per-10,000-residents
accessibility metric per ward.

## Tools
Python (Streamlit, geopandas, matplotlib), deployed on Streamlit Community Cloud

## Files
- app.py — dashboard application code
- newcastle_gp_accessibility.geojson — ward-level dataset with computed metrics
- requirements.txt — dependencies for deployment
