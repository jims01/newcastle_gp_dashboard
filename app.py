
import streamlit as st
import geopandas as gpd

st.title("Newcastle GP Accessibility Dashboard")
st.write("Exploring healthcare accessibility across Newcastle's electoral wards")


data = gpd.read_file("newcastle_gp_accessibility.geojson")
st.write(data[['WD23NM', 'total_population', 'gp_count', 'gp_per_10k']])

st.subheader("Newcastle Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Wards", len(data))
col2.metric("Total GP Surgeries", int(data['gp_count'].sum()))
col3.metric("Wards with No GP Access", int((data['gp_per_10k'] == 0).sum()))

st.subheader("Explore a specific ward")

selected_ward = st.selectbox("Choose a ward:", data['WD23NM'].sort_values())

ward_data = data[data['WD23NM'] == selected_ward]

st.write(f"*Population:* {ward_data['total_population'].values[0]:,}")
st.write(f"*GPs within 1km:* {ward_data['gp_count'].values[0]}")
st.write(f"*GPs per 10,000 residents:* {ward_data['gp_per_10k'].values[0]:.2f}")

import matplotlib.pyplot as plt

st.subheader("Map View")

fig, ax = plt.subplots(figsize=(6, 6))
data.plot(column='gp_per_10k', cmap='RdYlGn', edgecolor='black', linewidth=0.3, legend=True, ax=ax)

# Highlight the selected ward with a thick blue outline
ward_data.plot(ax=ax, facecolor='none', edgecolor='blue', linewidth=3)

ax.set_title(f"GP Accessibility — {selected_ward} highlighted")
ax.axis('off')
st.pyplot(fig)

