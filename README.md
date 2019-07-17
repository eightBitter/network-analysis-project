# Network Analysis Project

This repo contains scripts, metadata documentation, and sample data for a network analysis project I worked on for an NCSU PhD student. The goal of this project was to gather keyword data from a curated list of journals from a variety of domains such as Health, Real Estate, and Environment, normalize the heterogenous data, run analysis, and demonstrate, through network visualizations, that these domains are becoming interdisciplinary.

The assets in this repo reflect the process of gathering and normalizing the heterogenous data. Assets are organized into three folders - ebsco, proquest, and scienceDirect. Each folder represents one of the three major journal providers we gathered keyword data from. I organized assets in this way because each provider had a unique data format, which meant building unique tools and processes for normalizing the data. Each folder has the following:

- data dictionary detailing each data element in the normalized dataset
- Python script used to reformat the original data format to a CSV of targeted data
- a Markdown file detailing the gathering and normalization processes
- an OpenRefine tasks JSON file of example normalization tasks performed using OpenRefine
- a sample input data file (proquest has two, which is explained in the Markdown file)
