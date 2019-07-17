# Ebsco data gathering and processing

## Gathering Data

1. go to journal page; click on "Full Text" link
2. change the search perimeters to just the journal name (remove "AND FT Y")
3. change the Publication Date range to the desired range
4. click "Share" -> "Email link to download exported results" -> Select "Generic bibliographic management format"

## Data Cleaning Process

1. run `ebsco-parser.py`; this should reformat the data as a CSV. Make sure your input file name in the Python script matches your data file
2. open CSV in Excel; add column "Domain"; insert domain for the journal
3. create new project in OpenRefine; import data file
4. clean data in OpenRefine
  - consult `ebsco-data-dictionary.xlsx` for desired data formatting
  - consult `ebsco-openRefine-tasks.json` for tasks that have been used in the past. This can be imported into OpenRefine to perform repeat tasks, but first make sure the imported tasks will do what you want them to do (sometimes the format is slightly different between each EBSCO journal dataset)
5. once the data is cleaned, export the data as CSV

## Data Aggregating Process

1. once you have cleaned the data for all EBSCO journals, move the data files into a single folder
2. create an aggregated data file. I used the following Unix command: `mkdir combined && head -1 american-journal-health-promotion-cleaned.csv > combined/ebsco-combined.csv && tail -n +2 -q *.csv >> combined/ebsco-combined.csv`
  - this command takes the header from the specified CSV and adds the header to a new CSV, then compiles all data from all CSV files in the directory (except headers) and adds the compiled data to the new CSV. Essentially this command makes sure you aggregate only one header

## Notes

- importing data from .xlsx format seems to be better for character encoding than importing a CSV to OpenRefine
  - if you choose this approach, you'll have to reformat the numbers to text before importing to OpenRefine
