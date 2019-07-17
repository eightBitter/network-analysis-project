# ScienceDirect data gathering and processing

## Gathering Data

1. go to journal page; navigate to "All issues"; select an issue; select each article in the issue
2. click "Export citations" -> "Export citation and abstract to RIS"

## Data Aggregating Process

1. once you have downloaded the data for all ScienceDirect journals, move the data files into a single folder
2. create an aggregated data file. I used the following Unix command: `awk 'FNR==1{print ""}1' *.ris > combined/combined.ris`
  - I adapted this command from [stackoverflow](https://stackoverflow.com/questions/8183191/concatenating-files-and-insert-new-line-in-between-files)
  - to be honest, I'm not familiar with `awk`, but I know that this command concatenates all of the .ris files and adds a new line at the end of each concatenated dataset, which is needed to successfully run the following Python script

## Data Cleaning Process

1. run `scienceDirect-parser.py`; this should reformat the data as a CSV. Make sure your input file name in the Python script matches your data file
2. open CSV in Excel; add column "Domain"; insert domain for the journal
3. create new project in OpenRefine; import data file
4. clean data in OpenRefine
  - consult `scienceDirect-data-dictionary.xlsx` for desired data formatting
  - consult `scienceDirect-openRefine-tasks.json` for tasks that have been used in the past. This can be imported into OpenRefine to perform repeat tasks, but first make sure the imported tasks will do what you want them to do (sometimes the format is slightly different between each ScienceDirect journal dataset)
5. once the data is cleaned, export the data as CSV

## Notes

- importing data from .xlsx format seems to be better for character encoding than importing a CSV to OpenRefine
  - if you choose this approach, you'll have to reformat the numbers to text before importing to OpenRefine
