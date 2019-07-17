# Proquest data gathering and processing

## Gathering Data

1. go to journal page; click on "Advanced Search" link
2. change the "Publication date" range to the desired range
3. set "Items per page" to 100 to minimize the number of pages you have to click through
4. click the button that selects all results; repeat this for all pages
5. "Save" results as XSL
  - this gets you most of the metadata, but does not include author-supplied keywords
6. "Save" results as text -> Full text
  - this gets you a full text document in .txt format that you use to extract the keywords
  - before you go through the trouble of doing this and following gathering steps, you might want to spot check articles in the selection. If there are no keywords present, then it's not worth doing this and following gathering steps
  - sometimes when you click on Save -> text, you won't see "Full text" as an option. From what I can gather, this is because some journals only publish full text articles as PDFs, so there's no text document available
  - make sure to clear out your selection in Proquest's platform before gathering for another Proquest journal. Sometimes Proquest saves your selection even after you close out of their website
  - interesting tidbit: if there's full text available (even if we don't have access to the full text), we can download a "full text" document. The document won't have the full text, but it will have semi-structured data for titles, abstracts, and keywords (when available)

## Data Cleaning Process

1. run `proquest-keyword-extract.py`; this extracts titles and keywords from the full text document and creates a CSV with the extracted data. Make sure that the input file name in the Python script matches your data file
2. copy and paste the keywords column to your XSL data file
  - the XSL and CSV files should be pre-sorted, so if you just copy and paste your keywords should match the correct article titles
  - no need to do anything with the title column in the CSV - this is purely a match point to join the keywords to the XSL data file
  - you can do a quick find and replace on the keywords column while in Excel if you want, or you can do this in OpenRefine
3. add column "Domain"; insert domain for the journal
4. before importing into OpenRefine, remove unneeded columns and make sure that your remaining columns are organized in the same order as shown in the data dictionary: `proquest-data-dictionary.xlsx`
    - you will want to rename those remaining columns to conform to the labels in the data dictionary, but this can be done either in Excel or in OpenRefine
5. create new project in OpenRefine; import data file
6. clean data in OpenRefine
  - consult `proquest-data-dictionary.xlsx` for desired data formatting
  - consult `proquest-openRefine-tasks.json` for tasks that have been used in the past. This can be imported into OpenRefine to perform repeat tasks, but first make sure the imported tasks do what you want them to do
7. once the data is cleaned, export the data as CSV

## Data Aggregating Process

1. once you have cleaned the data for all Proquest journals, move the data files into a single folder
2. create an aggregated data file. I used the following Unix command: `mkdir combined && head -1 journal-housing-research-full.csv > combined/proquest-combined.csv && tail -n +2 -q *.csv >> combined/proquest-combined.csv`
  - this command takes the header from the specified CSV and adds the header to a new CSV, then compiles all data from all CSV files in the directory (except headers) and adds the compiled data to the new CSV. Essentially this command makes sure you aggregate only one header
